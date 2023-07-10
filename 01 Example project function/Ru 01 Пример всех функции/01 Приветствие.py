import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('Старт'))
Moko.Stage(stars('*'))

Moko.Messenger('set', 'Приветствие.jpg', 'Дорогой пользователь!\n'
                                         'Спасибо, что установили MOKO SE.\n'
                                         'Приятного пользования!')

Moko.Stage(stars('*'))
Moko.Stage(stars('Следующий SCRIPT'))
Moko.Stage(stars('*'))
Moko.EndScript()