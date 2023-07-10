import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))


Moko.Stage('Utility', 'Utility')
Moko.Messenger('set', 'set', 'This script demonstrates how the Utility function works. For example, '
                             'utility \'\'ExUtility\'\', which has two modes of operation and one command.')
Moko.Messenger('set', 'set', 'The \'\'set\'\' mode sets a specific command to the utility. '
                             'In this utility, the command is \'\'text\'\'. '
                             'The result of the \'\'text\'\' command is a window with the command name and two buttons: '
                             '\'\'OK\'\' and \'\'Cancel\'\'. Clicking any of them will close the window.')
Moko.Utility('ExUtility', 'set', 'text')
Moko.Messenger('set', 'get', 'The \'\'get\'\' mode returns a value of type \'\'boolean\'\'. Clicking on \'\'OK\'\' returns the value '
                             'True, with \'\'Cancel\'\' - False.')
resp = Moko.Utility('ExUtility', 'get', 'text', 'boolean')
if resp:
    Moko.Messenger('set', 'True', 'You clicked on the \'\'OK\'\' button.')
    Moko.Report("exutility", 'set', 'string', 'You clicked on \'\'OK\'\' and ExUtility returned True.')
else:
    Moko.Messenger('set', 'False', 'You clicked on the \'\'Cancel\'\' button.')
    Moko.Report("exutility", 'set', 'string', 'You clicked on \'\'Cancel\'\' and ExUtility returned False.')

Moko.Messenger('set', 'command', 'The \'\'text\'\' command has the ability to pass any information to the popup '
                                 'is the same as in the driver. \'\'text = Hello, World!\'\'')
Moko.Utility('ExUtility', 'set', 'text=Hello, World!')
Moko.Report("exutility_1", 'set', 'string', 'The script completed successfully.')


Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript('failed')