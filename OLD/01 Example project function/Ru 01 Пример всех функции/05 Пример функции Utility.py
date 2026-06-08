import MOKO
from MOSC import stars

MOKO.Stage(stars('*'))
MOKO.Stage(stars('Новый SCRIPT'))
MOKO.Stage(stars('*'))

MOKO.Stage('Utility', 'Utility')
MOKO.Messenger('set', 'set', 'В этом скрипте демонстрируется принцип работы функции Utility. Для примера используется '
                         'утилита \'\'ExUtility\'\', имеющая два режима работы и одну команду. ')
MOKO.Messenger('set', 'set', 'Режим \'\'set\'\' задает определенную команду в утилиту. В данной утилите - команда \'\'text\'\'. '
                         'Результатом команды \'\'text\'\' является окно с названием команды и  двумя конпками: \'\'OK\'\' и '
                         '\'\'Cancel\'\'. Нажатие любой из них приведёт к закрытию окна.')
MOKO.Utility('moko_example', 'set', 'text')

MOKO.Messenger('set', 'get', 'Режим \'\'get\'\' возвращает значение типа \'\'booleanм. При нажатии на \'\'OK\'\' возвращает значение '
                         'True, при \'\'Cancel\'\' - False.')
resp = MOKO.Utility('moko_example', 'get', 'text', 'boolean')
if resp:
    MOKO.Messenger('set', 'True', 'Вы нажали на кнопку \'\'OK\'\'.')
    MOKO.Report("exutility", 'set', 'string', 'Вы нажали на \'\'OK\'\' и ExUtility вернула значение True.')
else:
    MOKO.Messenger('set', 'False', 'Вы нажали на кнопку \'\'Cancel\'\'.')
    MOKO.Report("exutility", 'set', 'string', 'Вы нажали на \'\'Cancel\'\' и ExUtility вернула значение False.')
MOKO.Messenger('set', 'command', 'Команда \'\'text\'\' имеет возможность передать какую-либо информацию во всплывающее окно '
                             'так же, как и в драйвере. \'\'text=Hello,World!\'\' ')
MOKO.Utility('moko_example', 'set', 'text=Hello, World!')
MOKO.Report("exutility_1", 'set', 'string', 'Скрипт успешно завершён.')

MOKO.Stage(stars('*'))
MOKO.Stage(stars('Следующий SCRIPT'))
MOKO.Stage(stars('*'))

MOKO.EndScript('failed')
