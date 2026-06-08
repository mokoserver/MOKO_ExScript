import MOKO

MOKO.StageSeparator()
MOKO.StageSeparator('NEW SCRIPT')
MOKO.StageSeparator()


MOKO.StageUtility('Utility')
MOKO.MessageSet( 'set',
                 'This script demonstrates how the Utility function works. For example, \n'
                             'utility \'\'ExUtility\'\', which has two modes of operation and one command.')
MOKO.MessageSet( 'set',
                 'The \'\'set\'\' mode sets a specific command to the utility. \n'
                       'In this utility, the command is \'\'text\'\'. \n'
                       'The result of the \'\'text\'\' command is a window with the command name and two buttons: \n'
                       '\'\'OK\'\' and \'\'Cancel\'\'. Clicking any of them will close the window.')
MOKO.UtilitySet('moko_example',
             'text')

MOKO.MessageSet( 'get', 'The \'\'get\'\' mode returns a value of type \'\'boolean\'\'. Clicking on \'\'OK\'\' returns the value '
                             'True, with \'\'Cancel\'\' - False.')

resp = MOKO.UtilityGet('moko_example', 'text', 'bool')

if resp:
    MOKO.MessageSet( 'True',
                     'You clicked on the \'\'OK\'\' button.')
    MOKO.ReportSetString("exutility",
                         'You clicked on \'\'OK\'\' and ExUtility returned True.')
else:
    MOKO.MessageSet( 'False',
                     'You clicked on the \'\'Cancel\'\' button.')
    MOKO.ReportSetString("exutility",
                         'You clicked on \'\'Cancel\'\' and ExUtility returned False.')

MOKO.MessageSet( 'command',
                 'The \'\'text\'\' command has the ability to pass any information to the popup \n'
                      'is the same as in the driver. \'\'text = Hello, World!\'\'')
MOKO.UtilitySet('moko_example',  'text = Hello, World!')

MOKO.ReportSetString("exutility_1",
                     'The script completed successfully.')


MOKO.StageSeparator()
MOKO.StageSeparator('NEXT SCRIPT')
MOKO.StageSeparator()

MOKO.ScriptEnd('failed')