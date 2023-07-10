import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('Новый SCRIPT'))
Moko.Stage(stars('*'))

Moko.Stage('Utility', 'Utility')
Moko.Messenger('set', 'set', 'В этом скрипте демонстрируется принцип работы функции Utility. Для примера используется '
                         'утилита \'\'ExUtility\'\', имеющая два режима работы и одну команду. ')
Moko.Messenger('set', 'set', 'Режим \'\'set\'\' задает определенную команду в утилиту. В данной утилите - команда \'\'text\'\'. '
                         'Результатом команды \'\'text\'\' является окно с названием команды и  двумя конпками: \'\'OK\'\' и '
                         '\'\'Cancel\'\'. Нажатие любой из них приведёт к закрытию окна.')
Moko.Utility('ExUtility', 'set', 'text')

Moko.Messenger('set', 'get', 'Режим \'\'get\'\' возвращает значение типа \'\'booleanм. При нажатии на \'\'OK\'\' возвращает значение '
                         'True, при \'\'Cancel\'\' - False.')
resp = Moko.Utility('ExUtility', 'get', 'text', 'boolean')
if resp:
    Moko.Messenger('set', 'True', 'Вы нажали на кнопку \'\'OK\'\'.')
    Moko.Report("exutility", 'set', 'string', 'Вы нажали на \'\'OK\'\' и ExUtility вернула значение True.')
else:
    Moko.Messenger('set', 'False', 'Вы нажали на кнопку \'\'Cancel\'\'.')
    Moko.Report("exutility", 'set', 'string', 'Вы нажали на \'\'Cancel\'\' и ExUtility вернула значение False.')
Moko.Messenger('set', 'command', 'Команда \'\'text\'\' имеет возможность передать какую-либо информацию во всплывающее окно '
                             'так же, как и в драйвере. \'\'text=Hello,World!\'\' ')
Moko.Utility('ExUtility', 'set', 'text=Hello, World!')
Moko.Report("exutility_1", 'set', 'string', 'Скрипт успешно завершён.')

Moko.Stage(stars('*'))
Moko.Stage(stars('Следующий SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript('failed')
