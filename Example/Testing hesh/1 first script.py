import MOKO
from time import sleep

#Region Test script:$1.1
#description: Script;Point;Result

#hesh first point$1.1: First;1;Good
#hesh second point$1.1: First;2;Good
#hesh third point$1.1: First;3;Good

MOKO.Program('tree', 'set', 'select = first point$1.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = second point$1.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = third point$1.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Test script:$1.1

#Region Test script:$1.2
#description: Script;Point;Result

#hesh first point$1.2: First;4;Good
#hesh second point$1.2: First;5;Good
#hesh third point$1.2: First;6;Good

MOKO.Program('tree', 'set', 'select = first point$1.2')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = second point$1.2')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = third point$1.2')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Test script:$1.2

MOKO.EndScript()