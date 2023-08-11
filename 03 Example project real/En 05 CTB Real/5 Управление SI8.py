import MOKO

MOKO.Stage("Начало скрипта")

#Region 5.1 Статус
#hesh Управление SI8

MOKO.Messenger('set', 'SI8.jpg', 'В текущем скрипте будет продемонстрирована работа с SI8.', '', '5')
MOKO.Messenger('set', 'SI8.jpg', 'Узнаем текущее время.' '', '5')
TimeNow = MOKO.Driver('SI8', 'get', 'UTC', 'string')
MOKO.Messenger('set', 'SI8.jpg', f'Текущее время - {TimeNow}.', '', '3')

MOKO.Report('TimeNow', 'set', 'string', f'{TimeNow}')

MOKO.Program('tree', 'set', 'select = ' + 'Управление SI8')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion 5.1 Статус

MOKO.Stage("Конец скрипта")
MOKO.EndScript()

