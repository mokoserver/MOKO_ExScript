import MOKO
from time import sleep

#Region Test script:$2.1
#description: Script;Point;Result

#hesh first point$2.1: Second;1;Good
#hesh second point$2.1: Second;2;Good
#hesh third point$2.1: Second;3;Good

MOKO.Program('tree', 'set', 'select = first point$2.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = second point$2.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = third point$2.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Test script:$2.1

MOKO.EndScript()