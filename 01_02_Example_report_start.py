import MokoRequestLib as Moko
from MokoFormatedLibrary import stars, choice_language

Moko.Stage(stars('*'))
Moko.Stage(stars('START'))
Moko.Stage(stars('*'))

language = choice_language()
if language == 'English (default)':
    Moko.Messenger('set', 'Welcome message', 'Dear User!\nThis project demonstrates the implementation of the Report function.\nEnjoyable using!')
elif language == 'Russian':
    Moko.Messenger('set', 'Приветственное сообщение', 'Уважаемый пользователь!\nЭтот проект демонстрирует реализацию функции Report.\nПриятного использования!')

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))
Moko.EndScript()