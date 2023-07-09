import MOKO

MOKO.Plugin("Graph", 'close', '')

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

if language == 'English':
    MOKO.Messenger('set', 'Farewell.jpg', 'You have looked at the work of the Graph plugin. Good luck!')
elif language == 'Русский':
    MOKO.Messenger('set', 'Farewell.jpg', 'Вы посмотрели на работу плагина Graph. Удачи!')


MOKO.EndScript()