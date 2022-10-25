import MOKO
from time import sleep

#Region Test script:$4.1
#description: Script;Point;Result

#hesh  $4.1: Fourth;1;Good
#hesh  $4.2: Fourth;2;Good
#hesh  $4.3: Fourth;3;Good

MOKO.Program('tree', 'set', 'select =  $4.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select =  $4.2')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select =  $4.3')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Test script:$4.1

MOKO.EndScript()