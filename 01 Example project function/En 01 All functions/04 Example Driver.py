import MOKO

MOKO.StageSeparator()
MOKO.StageSeparator('NEW SCRIPT')
MOKO.StageSeparator()

MOKO.StageDriver('*Driver*')
MOKO.MessageSet('Driver_info',
                'This script describes how the Driver function works.\n'
                'For example the \'\'ExDriver\'\' driver is used, which has several \n'
                'modes of operation, which will act further.')

MOKO.MessageSet( 'set',
                 'The \'\'set\'\' mode sets a specific command to the driver. '
                 'This ExDriver driver has the command \'\'value\'\'. '
                             'This way you can enter your own value into the driver')

MOKO.DriverSet('ExDriver','value = 5')

MOKO.MessageSet( 'get',
                 'The \'\'get\'\' mode returns the value you entered.')

value = MOKO.DriverGet('ExDriver', 'value', 'string')

MOKO.MessageSet( 'True',
                 f'You entered {value}.')

MOKO.ReportSetString("exdriver",
                     f'You entered {value}.')

MOKO.MessageSet( 'init',
                 'In \'\'init\'\' mode, the driver initialization window appears on the screen. \n'
                        'Since there is no device, click on the \'\'Cancel\'\' button.')

MOKO.DriverInit('ExDriver')

MOKO.ReportSetString("exdriver_1", 'The script completed successfully.')

MOKO.StageSeparator()
MOKO.StageSeparator('NEXT SCRIPT')
MOKO.StageSeparator()

MOKO.ScriptEnd('passed')