import MOKO
from MOSC import stars
import time

MOKO.StageSeparator()
MOKO.StageSeparator('NEW SCRIPT')
MOKO.StageSeparator()

language = MOKO.ReportGet("language",  'string')

MOKO.PluginInit('ExPlugin')

time.sleep(5)

MOKO.StagePlugin('*Plugin*')
MOKO.MessageSet( 'Plugin_info', 'This script describes how the Plugin function works. For example '
                                     'the plugin \'\'ExPlugin\'\' is used, which has 2 modes of operation: '
                                     '\'\'set\'\' and \'\'get\'\'.')
MOKO.MessageSet( 'Set Number1|2', 'The \'\'Number1|2\'\' command sets the number to Number1 or Number2 '
                                       'in the Main window. For this after the command = and the number '
                                       'to be written. By default, the numbers Number1 and Number2 are zero.')

MOKO.PluginSet('ExPlugin', 'Number1=9')
MOKO.PluginSet('ExPlugin', 'Number2=14')

MOKO.MessageSet( 'Get Sum',
                 'The \'\'Sum\'\' command returns the sum from the Sum field in the Main window.')

sum = MOKO.PluginGet('ExPlugin',  'Sum', 'string')
MOKO.MessageSet( 'Sum', f'Sum: {sum}')
MOKO.ReportSetString("explugin_1",  f'{sum}')

MOKO.MessageSet( 'Set String', 'The \'\'Set String\'\' command writes a string to the ExPlugin. To do this, after '
                                    'command is set = and the information to be recorded. '
                                    'The information is displayed in the String field in the Main window.')
MOKO.PluginSet('ExPlugin', 'String=Hello, World!')
MOKO.MessageSet('set', 'Get String', 'The Get String command returns a string from the String field '
                                    'in the Main window.')

a = MOKO.PluginGet('ExPlugin', 'String', 'string')

MOKO.MessageSet('String', f'String from ExPlugin: {a}')

MOKO.ReportSetString("explugin", f'{a}')

MOKO.MessageSet( 'Set Screenshot', 'The \'\'Screenshot\'\' command takes a screenshot of the plugin, '
                                        'whose name consists of'
                                        'date and time at the moment of the screenshot. '
                                        'The screenshot is saved in a separate folder '
                                        'App/screenshots in ExPlugin root directory')

MOKO.PluginSet('ExPlugin', 'Screenshot')
MOKO.Messenger('set', 'Set ChangeLedLoop', 'The \'\'ChangeLedLoop\'\' command changes the value'
                                           ' of the Led Loop indicator in the main window.')
MOKO.Plugin('ExPlugin', 'set', 'ChangeLedLoop')
MOKO.MessageSet('set', 'Set ShowTab', 'The command \'\'Showtab\'\' change displays the desired plugin '
                                     'window (Main | Graph | Info). '
                                     'To do this, after the command, put = and the name of the required window.')

MOKO.PluginSet('ExPlugin', 'ShowTab=Info')

time.sleep(10)
MOKO.PluginSet('ExPlugin', 'ShowTab=Graph')
time.sleep(3)

MOKO.MessageSet( 'Set Graph', 'The \'\'Graph\'\' command starts or stops a graph in the Graph window. '
                                   'To start after command \'\'Graph\'\' is set =start, and for stop =stop.')

MOKO.PluginSet('ExPlugin', 'Graph=start')

MOKO.MessageSet( 'Get InstantScreenshot', 'The \'\'InstantScreenshot\'\' command returns a screenshot'
                                               ' of the ExPlugin window.')
screen = MOKO.Plugin('ExPlugin', 'get', 'InstantScreenshot', 'string')
MOKO.ReportSetPicture("explugin_2", screen)
MOKO.PluginSet('ExPlugin', 'Graph=stop')
MOKO.ReportSetString("explugin_3", 'The script completed successfully.')

MOKO.StageSeparator()
MOKO.StageSeparator('NEXT SCRIPT')
MOKO.StageSeparator()

MOKO.ScriptEnd()