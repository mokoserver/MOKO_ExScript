import MOKO
from time import sleep

#Region Second script:

#hesh first point$2.1
#hesh second point$2.1
#hesh third point$2.1

MOKO.Program('tree', 'set', 'select = first point$2.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = second point$2.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = third point$2.1')
sleep(0.5)
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Second script:

MOKO.EndScript()