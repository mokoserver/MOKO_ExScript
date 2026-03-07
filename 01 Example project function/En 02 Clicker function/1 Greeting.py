import MOKO
from MOSC import stars

MOKO.Stage(stars('*'))
MOKO.Stage(stars('MOKO Clicker'))
MOKO.Stage(stars('*'))


MOKO.Messenger('set', 'Greeting#@hello',
               'This presentation will show 3 commands, but there are more commands. '
               'The first command is to get a screenshot of the screen, '
               'the second command is to specify the image path and '
               'the last command is to get the image from the specified path.')

#Region Status
#hash Greeting

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Region Status

MOKO.EndScript()