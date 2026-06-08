import MOKO

MOKO.Stage("Начало скрипта")

#Region 6.1 Этапы формирования:
#hash Автосохранение результатов
#hash Формирование протокола

MOKO.Messenger('set', 'Формирование протокола.jpg', 'Сейчас автоматически сформируется протокол.', '', '5')

MOKO.Program('tree', 'set', 'select = ' + 'Автосохранение результатов')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('Control', 'set', 'Save word report')
MOKO.Program('Control', 'set', 'Save project report')

MOKO.Program('tree', 'set', 'select = ' + 'Формирование протокола')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Stage('Формирование протокола завершено.', 'info')
#EndRegion 6.1 Этапы формирования:

MOKO.Stage("Конец скрипта")

MOKO.EndScript()
