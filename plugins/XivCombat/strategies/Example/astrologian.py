from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import FarCircle, select

card_map_arc = {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 2,
    6: 3,
}
card_map_range = {
    1: False,
    2: True,
    3: False,
    4: True,
    5: True,
    6: False,
}

cards = {
    1882,
    1883,
    1884,
    1885,
    1886,
    1887,
    1876,
    1877,
}


def select_res_target_key(actor):
    return actor.job.is_healer, actor.job.is_tank, actor.job.is_dps


def search_swift_res(data: 'LogicData'):
    if data.me.level < 12: return
    k = data.config['swift_res']
    if k == 'party':
        d = data.valid_party
    elif k == 'alliance':
        d = data.valid_alliance
    elif k == 'all':
        d = data.valid_players
    else:
        d = list()
    d = [member for member in d if not member.current_hp and 148 not in member.effects.get_dict() and data.actor_distance_effective(member) < 30]
    if d: return max(d, key=select_res_target_key)


def res_lv(data: 'LogicData'):
    match data.config['resource']:
        case define.RESOURCE_SQUAND:
            return 2
        case define.RESOURCE_NORMAL:
            return 1
        case define.RESOURCE_STINGY:
            return 0
        case _:
            return data.max_ttk > 15


def priority(data: 'LogicData', target, card_range):
    has_card = bool(target.effects.get_set().intersection(cards))
    dps = data.dps(target) * (2 if card_range == target.job.is_range else 1)
    if target.job.is_dps:
        order = 3
    elif target.job.is_tank:
        order = 2
    elif target.job.is_healer:
        order = 1
    else:
        order = 0
    return has_card, order, dps


def card_target(data: 'LogicData', card_id: int):
    if card_id not in card_map_range: return None
    card_range = card_map_range[card_id]
    party = [member for member in data.valid_party if data.actor_distance_effective(member) <= 30]
    if not len(party): return data.me
    return max(party, key=lambda member: priority(data, member, card_range))


ast_aoe = FarCircle(25, 5)


class AstrologianLogic(Strategy):
    name = "astrologian_logic"
    job = "Astrologian"
    default_data = {
        'swift_res': 'none',
    }

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int):
        match action_id:
            case 17055 | 7443:
                return action_id, card_target(data, data.gauge.held_card.raw_value).id
            case 7439:
                if 1224 not in data.effects and 1248 not in data.effects:
                    return UseAbility(7439, target_position=api.get_mo_location())
                else:
                    return UseAbility(8324)
            case _:
                mo_entity = api.get_mo_target()
                if mo_entity:
                    return UseAbility(action_id, target_id=mo_entity.id)

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        can_swing = 841 in data.effects or 167 in data.effects or not data.is_moving
        if not data[7561] or 167 in data.effects:
            res_target = search_swift_res(data)
            if res_target:
                if 167 in data.effects:
                    return UseAbility(3603, res_target.id)
                else:
                    return UseAbility(7561, ability_type=define.AbilityType.oGCD)
        if data.me.level >= 45 and can_swing:
            aoe_target, cnt = select(data, data.valid_enemies, ast_aoe)
            if cnt >= 3: return UseAbility(3615, aoe_target.id)
        if data.me.level >= 4:
            dot_status = 838 if data.me.level < 46 else 843 if data.me.level < 72 else 1881
            for enemy in data.valid_enemies:
                if data.actor_distance_effective(enemy) <= 25 and not enemy.effects.has(dot_status, data.me.id):
                    return UseAbility(3599, enemy.id)
        if can_swing and data.target_distance <= 25:
            return UseAbility(3596)

    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        res = res_lv(data)
        arcs = {arc.raw_value for arc in data.gauge.arcanums}
        if res and not data[16552] and 0 not in arcs and data.max_ttk >= 30:
            return UseAbility(16552)
        if data.gauge.held_card.raw_value:
            send_card = res or not data[3590]
            send_target = card_target(data, data.gauge.held_card.raw_value) if send_card else None
            held = card_map_arc[data.gauge.held_card.raw_value]
            if 0 in arcs and held in arcs:
                if data[3593] < 60:
                    return UseAbility(3593)
                elif send_card:
                    return UseAbility(7443, send_target.id)
            elif send_card:
                if held in arcs:
                    return UseAbility(7443, send_target.id)
                else:
                    return UseAbility(17055, send_target.id)
        else:
            if not data[3590]:
                return UseAbility(3590)
            elif not data[7448]:
                return UseAbility(7448)
        if data.me.current_mp <= 7000 and not data[7562]:
            return UseAbility(7562)
