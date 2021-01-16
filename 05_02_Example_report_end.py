import MokoRequestLib as Moko
from MokoFormatedLibrary import stars, choice_language


Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

language = choice_language()

if language == 'English (default)':
    Moko.Messenger('set', 'Farewell message', 'This project demonstrated how the Report function works. Thanks for using MOKO SE. Good luck!')

elif language == 'Russian':
    Moko.Messenger('set', 'Завершающий скрипт', 'Данный проект продемонстрировал принцип работы функции Report. Спасибо за использование MOKO SE. Удачи!')

Moko.Stage(stars('*'))
Moko.Stage(stars('END'))
Moko.Stage(stars('*'))

Moko.EndScript()
