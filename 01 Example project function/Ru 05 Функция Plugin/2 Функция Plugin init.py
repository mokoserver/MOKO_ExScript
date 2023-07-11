import MOKO

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Plugin init

MOKO.Messenger('set', 'Plugin - init.png', 'В данном скрипте будет продемонстрирована команда \'\'init\'\', '
                                           'которая запускает плагин.')


MOKO.Plugin("Graph", 'init', '')

MOKO.Program('tree', 'set', 'select = ' + 'Plugin init')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()
