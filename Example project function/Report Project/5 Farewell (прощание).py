import MOKO

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

if language == 'English':
    MOKO.Messenger('set', 'Farewell.jpg', 'That\'s all! Good luck!')
elif language == 'Русский':
    MOKO.Messenger('set', 'Farewell.jpg', 'На этом всё! Удачи!')


MOKO.EndScript()