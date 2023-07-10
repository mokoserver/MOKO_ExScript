import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

Moko.Stage('*Driver*', 'Driver')
Moko.Messenger('set', 'Driver_info', 'This script describes how the Driver function works. For example '
                                     'the \'\'ExDriver\'\' driver is used, which has several modes of operation,'
                                     'which will act further.')
Moko.Messenger('set', 'set', 'The \'\'set\'\' mode sets a specific command to the driver. This ExDriver driver has'
                             'the command \'\'value\'\'. '
                             'This way you can enter your own value into the driver')
Moko.Driver('ExDriver', 'set', 'value = 5')
Moko.Messenger('set', 'get', 'The \'\'get\'\' mode returns the value you entered.')
value = Moko.Driver('ExDriver', 'get', 'value', 'string')
Moko.Messenger('set', 'True', f'You entered {value}.')
Moko.Report("exdriver", 'set', 'string', f'You entered {value}.')
Moko.Messenger('set', 'init', 'In \'\'init\'\' mode, the driver initialization window appears on the screen. '
                              'Since there is no device, click on the \'\'Cancel\'\' button.')
Moko.Driver('ExDriver', 'init', '')
Moko.Report("exdriver_1", 'set', 'string', 'The script completed successfully.')

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript('passed')