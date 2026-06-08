import MOKO
import MGPH

#Region Status
#hash Plugin get

MOKO.Messenger('set', 'Plugin - get.png', 'The current script will demonstrate the \'\'get\'\' command, '
                                          'which receives data from the plugin. '
                                          'In the scripts will be made a screenshot.')


screen = MGPH.GetScreenshotWindow()
MOKO.Report("Screenshot_1_All", 'set', 'picture', screen)

MOKO.Program('tree', 'set', 'select = ' + 'Plugin get')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()
