import MOKO
from MOSC import stars

MOKO.Stage(stars('*'))
MOKO.Stage(stars('NEW SCRIPT'))
MOKO.Stage(stars('*'))


MOKO.Stage('Utility', 'Utility')
MOKO.Messenger('set', 'set', 'This script demonstrates how the Utility function works. For example, '
                             'utility \'\'ExUtility\'\', which has two modes of operation and one command.')
MOKO.Messenger('set', 'set', 'The \'\'set\'\' mode sets a specific command to the utility. '
                             'In this utility, the command is \'\'text\'\'. '
                             'The result of the \'\'text\'\' command is a window with the command name and two buttons: '
                             '\'\'OK\'\' and \'\'Cancel\'\'. Clicking any of them will close the window.')
MOKO.Utility('moko_example', 'set', 'text')
MOKO.Messenger('set', 'get', 'The \'\'get\'\' mode returns a value of type \'\'boolean\'\'. Clicking on \'\'OK\'\' returns the value '
                             'True, with \'\'Cancel\'\' - False.')
resp = MOKO.Utility('moko_example', 'get', 'text', 'boolean')
if resp:
    MOKO.Messenger('set', 'True', 'You clicked on the \'\'OK\'\' button.')
    MOKO.Report("exutility", 'set', 'string', 'You clicked on \'\'OK\'\' and ExUtility returned True.')
else:
    MOKO.Messenger('set', 'False', 'You clicked on the \'\'Cancel\'\' button.')
    MOKO.Report("exutility", 'set', 'string', 'You clicked on \'\'Cancel\'\' and ExUtility returned False.')

MOKO.Messenger('set', 'command', 'The \'\'text\'\' command has the ability to pass any information to the popup '
                                 'is the same as in the driver. \'\'text = Hello, World!\'\'')
MOKO.Utility('moko_example', 'set', 'text=Hello, World!')
MOKO.Report("exutility_1", 'set', 'string', 'The script completed successfully.')


MOKO.Stage(stars('*'))
MOKO.Stage(stars('NEXT SCRIPT'))
MOKO.Stage(stars('*'))

MOKO.EndScript('failed')