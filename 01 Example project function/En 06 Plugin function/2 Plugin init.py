import MOKO

#Region Status
#hesh Plugin init

MOKO.Messenger('set', 'Plugin - init.png', 'This script will demonstrate the \'\'init\'\' command, '
                                           'which starts the plugin.')

MOKO.Plugin("Graph", 'init', '')

MOKO.Program('tree', 'set', 'select = ' + 'Plugin init')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()
