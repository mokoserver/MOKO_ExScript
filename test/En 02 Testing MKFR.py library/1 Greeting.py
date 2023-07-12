import MOKO
from MOSC import stars

MOKO.Stage(stars('*'))
MOKO.Stage(stars('MOKO Testing Messenger picture'))
MOKO.Stage(stars('*'))


MOKO.Messenger('set', 'Greeting#@hello', 'This script will test inserting images into MOKO.Messenger. '
                                         'All pictures are located in the directory C:\\MOKO SE\Data\Messenger pictures')

#Region Status
#hesh Greeting

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Region Status

MOKO.EndScript()