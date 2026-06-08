import MOKO

#Region Status
#hash Plugin close

MOKO.Messenger('set', 'Plugin - close.png', 'This script will demonstrate the \'\'close\'\' command, '
                                            'which closes the plugin.')

MOKO.Plugin('Graph', 'close', '')

MOKO.Program('tree', 'set', 'select = ' + 'Plugin close')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()
