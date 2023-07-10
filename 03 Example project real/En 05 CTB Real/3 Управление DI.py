import MOKO

MOKO.Stage("Начало скрипта")

#Region 3.1 Статус
#hesh Управление DI

MOKO.Messenger('set', 'МК210-301.png', 'В текущем скрипте будет продемонстрирована работа в дискретными входами (DI) МК210-301', '', '5')
MOKO.Messenger('set', 'МК210-301.png', 'Узнаем состояние DI с помощью драйвера. \'\'1\'\' - выход активен, '
                                      '\'\'0\'\' - выход неактивен.', '', '5')
DI_state = MOKO.Driver('MK210', 'get', 'DI', 'string')
MOKO.Messenger('set', 'МК210-301.png', f'Текущее состояние DI - {DI_state}.', '', '3')

MOKO.Report('DI_state', 'set', 'string', f'{DI_state}')

MOKO.Program('tree', 'set', 'select = ' + 'Управление DI')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion 3.1 Статус

MOKO.Stage("Конец скрипта")
MOKO.EndScript()

