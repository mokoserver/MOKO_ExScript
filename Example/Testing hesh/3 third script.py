import MOKO
from time import sleep

#Region Test script:

#hesh first point$3.1
#hesh second point$3.1
#hesh third point$3.1

MOKO.Program('tree', 'set', 'select = first point$3.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = second point$3.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = third point$3.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Test script:

MOKO.EndScript()