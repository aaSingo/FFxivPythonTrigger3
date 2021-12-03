from ..base import *


class Actions:

    class TrueThrust(ActionBase):
        """
Delivers an attack with a potency of (source.job==22?(source.level>=76?230:170):170).(source.job==22?(source.level>=76?
※Action changes to Raiden Thrust while under the effect of Draconian Fire.:):)
        """
        id = 75
        name = {'精准刺', 'True Thrust'}

    class VorpalThrust(ActionBase):
        """
Delivers an attack with a potency of (source.job==22?(source.level>=76?130:100):100).
Combo Action: True Thrust
Combo Potency: (source.job==22?(source.level>=76?280:250):250)
        """
        id = 78
        name = {'Vorpal Thrust', '贯通刺'}
        combo_action = 75

    class LifeSurge(ActionBase):
        """
Ensures critical damage for first weaponskill used while Life Surge is active.
Duration: 5s
Effect cannot be applied to damage over time.
Additional Effect: Absorbs a portion of damage dealt as HP(source.job==22?(source.level>=88?
Maximum Charges: 2:):)
>> 116, Life Surge, Next weaponskill will result in a critical hit with a portion of the resulting damage being absorbed as HP.
>> 2175, Life Surge, Next weaponskill will deal increased damage.
        """
        id = 83
        name = {'龙剑', 'Life Surge'}

    class PiercingTalon(ActionBase):
        """
Delivers a ranged attack with a potency of 150.
        """
        id = 90
        name = {'贯穿尖', 'Piercing Talon'}

    class Disembowel(ActionBase):
        """
Delivers an attack with a potency of (source.job==22?(source.level>=76?140:100):100).
Combo Action: True Thrust
Combo Potency: (source.job==22?(source.level>=76?250:210):210)
Combo Bonus: Grants Power Surge
Power Surge Effect: Increases damage dealt by 10%
Duration: 30s
>> 121, Disembowel, Piercing resistance is reduced.
>> 1914, Disembowel, Damage dealt is increased.
        """
        id = 87
        name = {'开膛枪', 'Disembowel'}
        combo_action = 75

    class FullThrust(ActionBase):
        """
Delivers an attack with a potency of 100.
Combo Action: Vorpal Thrust
Combo Potency: 400(source.level>=56?(source.job==22?
Combo Bonus: Grants Sharper Fang and Claw
Duration: 30s
Effect of Sharper Fang and Claw ends upon execution of any melee weaponskill.:):)
        """
        id = 84
        name = {'Full Thrust', '直刺'}
        combo_action = 78

    class LanceCharge(ActionBase):
        """
Increases damage dealt by 10%.
Duration: 20s
>> 1864, Lance Charge, Damage dealt is increased.
        """
        id = 85
        name = {'Lance Charge', '猛枪'}

    class Jump(ActionBase):
        """
Delivers a jumping attack with a potency of (source.job==22?(source.level>=54?320:250):250). Returns you to your original position after the attack is made.
(source.level>=68?(source.job==22?Additional Effect: Grants Dive Ready
Duration: 15s
:):)Cannot be executed while bound.
        """
        id = 92
        name = {'Jump', '跳跃'}

    class ElusiveJump(ActionBase):
        """
Executes a jump to a location 15 yalms behind you.
Cannot be executed while bound.
        """
        id = 94
        name = {'回避跳跃', 'Elusive Jump'}

    class DoomSpike(ActionBase):
        """
Delivers an attack with a potency of 110 to all enemies in a straight line before you.(source.job==22?(source.level>=82?
※Action changes to Draconian Fury when under the effect of Draconian Fire.:):)
        """
        id = 86
        name = {'Doom Spike', '死天枪'}

    class SpineshatterDive(ActionBase):
        """
Delivers a jumping attack with a potency of (source.job==22?(source.level>=54?250:190):190).
(source.job==22?(source.level>=84?Maximum Charges: 2
:):)Cannot be executed while bound.
        """
        id = 95
        name = {'Spineshatter Dive', '破碎冲'}

    class ChaosThrust(ActionBase):
        """
Delivers an attack with a potency of 100.
140 when executed from a target's rear.
Combo Action: Disembowel
Combo Potency: 220
Rear Combo Potency: 260
Combo Bonus: Damage over time
Potency: 40
Duration: 24s(source.level>=58?(source.job==22?
Combo Bonus: Grants Enhanced Wheeling Thrust
Duration: 30s
Effect of Enhanced Wheeling Thrust ends upon execution of any melee weaponskill.:):)
>> 1312, Chaos Thrust, Sustaining damage over time, as well as increased damage from target who executed Chaos Thrust.
>> 118, Chaos Thrust, Wounds are bleeding, causing damage over time.
        """
        id = 88
        name = {'Chaos Thrust', '樱花怒放'}
        combo_action = 87

    class DragonfireDive(ActionBase):
        """
Delivers a jumping fire-based attack with a potency of 300 to target and all enemies nearby it.
Cannot be executed while bound.
        """
        id = 96
        name = {'龙炎冲', 'Dragonfire Dive'}

    class BattleLitany(ActionBase):
        """
Increases critical hit rate of self and nearby party members by 10%.
Duration: 15s
>> 786, Battle Litany, Critical hit rate is increased.
>> 1414, Battle Litany, Damage dealt is increased.
        """
        id = 3557
        name = {'Battle Litany', '战斗连祷'}

    class FangAndClaw(ActionBase):
        """
Delivers an attack with a potency of 260.
300 when executed from a target's flank.
Can only be executed while under the effect of Sharper Fang and Claw.
        """
        id = 3554
        name = {'Fang and Claw', '龙牙龙爪'}

    class WheelingThrust(ActionBase):
        """
Delivers an attack with a potency of 260.
300 when executed from a target's rear.
Can only be executed while under the effect of Enhanced Wheeling Thrust.
        """
        id = 3556
        name = {'龙尾大回旋', 'Wheeling Thrust'}

    class Geirskogul(ActionBase):
        """
Delivers an attack to all enemies in a straight line before you with a potency of (source.job==22?(source.level>=90?250:200):200) for the first enemy, and 30% less for all remaining enemies.(source.level>=70?(source.job==22?
Additional Effect: Grants Life of the Dragon while under the full gaze of the first brood
※Action changes to Nastrond while under the effect of Life of the Dragon.:):)
        """
        id = 3555
        name = {'武神枪', 'Geirskogul'}

    class SonicThrust(ActionBase):
        """
Delivers an attack with a potency of 100 to all enemies in a straight line before you.
Combo Action: Doom Spike
Combo Potency: 120
Combo Bonus: Grants Power Surge
Power Surge Effect: Increases damage dealt by 10%
Duration: 30s
        """
        id = 7397
        name = {'Sonic Thrust', '音速刺'}
        combo_action = 86

    class DragonSight(ActionBase):
        """
Grants Right Eye to self, increasing damage dealt by 10%. Also grants target party member Left Eye, increasing damage dealt by 5% as long as target remains within 12 yalms.
Duration: 20s
        """
        id = 7398
        name = {'Dragon Sight', '巨龙视线'}

    class MirageDive(ActionBase):
        """
Delivers an attack with a potency of 200.
(source.level>=70?(source.job==22?Additional Effect: Strengthens the gaze of your Dragon Gauge by 1
:):)Can only be executed when Dive Ready.
        """
        id = 7399
        name = {'Mirage Dive', '幻象冲'}

    class Nastrond(ActionBase):
        """
Delivers an attack to all enemies in a straight line before you with a potency of (source.job==22?(source.level>=90?350:300):300) for the first enemy, and 30% less for all remaining enemies.
Can only be executed while under the effect of Life of the Dragon.
※This action cannot be assigned to a hotbar.
        """
        id = 7400
        name = {'死者之岸', 'Nastrond'}

    class CoerthanTorment(ActionBase):
        """
Delivers an attack with a potency of 100 to all enemies in a straight line before you.
Combo Action: Sonic Thrust
Combo Potency: 150(source.job==22?(source.level>=82?
Combo Bonus: Grants Draconian Fire
Duration: 30s:):)
        """
        id = 16477
        name = {'山境酷刑', 'Coerthan Torment'}
        combo_action = 7397

    class HighJump(ActionBase):
        """
Delivers a jumping attack with a potency of 400. Returns you to your original position after the attack is made.
Additional Effect: Grants Dive Ready
Duration: 15s
Cannot be executed while bound.
        """
        id = 16478
        name = {'高跳', 'High Jump'}

    class RaidenThrust(ActionBase):
        """
Delivers an attack with a potency of 260.
(source.job==22?(source.level>=90?Additional Effect: Sharpens the Firstminds' Focus by 1
:):)Can only be executed while under the effect of Draconian Fire.
※This action cannot be assigned to a hotbar.
        """
        id = 16479
        name = {'Raiden Thrust', '龙眼雷电'}

    class Stardiver(ActionBase):
        """
Delivers a jumping fire-based attack to target and all enemies nearby it with a potency of 500 for the first enemy, and 30% less for all remaining enemies.
Can only be executed while under the effect of Life of the Dragon.
Cannot be executed while bound.
        """
        id = 16480
        name = {'Stardiver', '坠星冲'}

    class DraconianFury(ActionBase):
        """
Delivers an attack with a potency of 130 to all enemies in a straight line before you.
(source.job==22?(source.level>=90?Additional Effect: Sharpens the Firstminds' Focus by 1
:):)Can only be executed while under the effect of Draconian Fire.
※This action cannot be assigned to a hotbar.
        """
        id = 25770
        name = {'Draconian Fury'}

    class HeavensThrust(ActionBase):
        """
Delivers an attack with a potency of 100.
Combo Action: Vorpal Thrust
Combo Potency: 430
Combo Bonus: Grants Sharper Fang and Claw
Duration: 30s
Effect of Sharper Fang and Claw ends upon execution of any melee weaponskill.
        """
        id = 25771
        name = {"Heavens' Thrust"}
        combo_action = 78

    class ChaoticSpring(ActionBase):
        """
Delivers an attack with a potency of 100.
140 when executed from a target's rear.
Combo Action: Disembowel
Combo Potency: 240
Rear Combo Potency: 280
Combo Bonus: Damage over time
Potency: 45
Duration: 24s
Combo Bonus: Grants Enhanced Wheeling Thrust
Duration: 30s
Effect of Enhanced Wheeling Thrust ends upon execution of any melee weaponskill.
>> 2719, Chaotic Spring, Sustaining damage over time.
        """
        id = 25772
        name = {'Chaotic Spring'}
        combo_action = 87

    class WyrmwindThrust(ActionBase):
        """
Delivers an attack to all enemies in a straight line before you with a potency of 370 for the first enemy, and 50% less for all remaining enemies.
Firstminds' Focus Cost: 2
        """
        id = 25773
        name = {'Wyrmwind Thrust'}
