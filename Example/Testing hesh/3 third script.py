import MOKO
from time import sleep

#Region Test script:$3.1
#description: Script;Point;Result

#hesh first point$3.1: Third;1;Good
#hesh second point$3.1: Third;2;Good
#hesh third point$3.1: Third;3;Good

MOKO.Program('tree', 'set', 'select = first point$3.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = second point$3.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = third point$3.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Test script:$3.1

MOKO.EndScript()