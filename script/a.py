from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *

def main():
    t = plugins.XivMemory.targets.focus
    if not t:raise Exception("No target")
    t_pos = t.pos
    m_pos = plugins.XivMemory.coordinate
    t_pos.x = m_pos.x
    t_pos.y = m_pos.y
    t_pos.z = m_pos.z

for i in range(100):
    main()
    sleep(0.5)
