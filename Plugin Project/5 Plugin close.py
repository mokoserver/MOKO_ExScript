import MOKO

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Plugin close

if language == "English":
    MOKO.Messenger('set', 'Plugin - close.png', 'This script will demonstrate the \'\'close\'\' command, '
                                                'which closes the plugin.')
elif language == "Русский":
    MOKO.Messenger('set', 'Plugin - close.png', 'В данном скрипте будет продемонстрирована команда \'\'close\'\', '
                                                'которая закрывает плагин.')

MOKO.Plugin('Graph', 'close', '')

MOKO.Program('tree', 'set', 'select = ' + 'Plugin close')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()