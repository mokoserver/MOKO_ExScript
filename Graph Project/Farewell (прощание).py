import MOKO

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

if language == 'English':
    MOKO.Messenger('set', 'Welcome message', 'You have looked at the work of the Graph plugin. Good luck!')
elif language == 'Русский':
    MOKO.Messenger('set', 'Приветствие', 'Вы посмотрели на работу плагина Graph. Удачи!')


MOKO.EndScript()