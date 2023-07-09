import MOKO


language = MOKO.Report("language", 'get', 'string', 'string', 'string')
if language == 'English':
    MOKO.Messenger('set', 'Farewell.jpg','It was MOKO Clicker presentation. Thank you for your attention!')
else:
    MOKO.Messenger('set', 'Farewell.jpg', 'Вам была продемонстрирована программа MOKO Clicker. Спасибо за внимание!')

#Region Status (Статус)
#hesh Farewell
MOKO.Program('tree', 'set', 'select = ' + 'Farewell')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()