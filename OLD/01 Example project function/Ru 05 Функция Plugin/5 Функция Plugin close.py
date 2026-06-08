import MOKO

#Region Status (статус)
#hash Plugin close

MOKO.Messenger('set', 'Plugin - close.png', 'В данном скрипте будет продемонстрирована команда \'\'close\'\', '
                                            'которая закрывает плагин.')

MOKO.Plugin('Graph', 'close', '')

MOKO.Program('tree', 'set', 'select = ' + 'Plugin close')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()
