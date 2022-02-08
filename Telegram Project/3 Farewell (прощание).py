import MOKO

#Region Status (статус)
#hesh Farewell

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

if language == 'English':
    MOKO.Messenger('set', 'Farewell.jpg', 'That\'s all! Good luck!')
elif language == 'Русский':
    MOKO.Messenger('set', 'Farewell.jpg', 'На этом всё! Удачи!')

MOKO.Program('tree', 'set', 'select = ' + 'Farewell')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status


MOKO.EndScript()