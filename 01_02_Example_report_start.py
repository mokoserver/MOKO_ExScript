import MokoRequestLib as Moko
from MokoFormatedLibrary import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('START'))
Moko.Stage(stars('*'))

language = Moko.Messenger('get', 'Language', 'Please select your language in dropdown:',
                          'choice=English(default);Русский;')
Moko.Report("language", 'set', 'string', language)
if language == 'English(default)':
    Moko.Messenger('set', 'Welcome message', 'Dear User!\nThis project demonstrates the implementation of the Report function.\nEnjoyable using!')
elif language == 'Русский':
    Moko.Messenger('set', 'Приветственное сообщение', 'Уважаемый пользователь!\nЭтот проект демонстрирует реализацию функции Report.\nПриятного использования!')

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))
Moko.EndScript()