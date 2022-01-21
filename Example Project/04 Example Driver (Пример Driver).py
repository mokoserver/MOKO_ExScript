import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

language = Moko.Report("language", 'get', 'string', 'string', 'string')

if language == 'English(default)':
    Moko.Stage('*Driver*', 'Driver')
    Moko.Messenger('set', 'Driver_info', 'This script describes how the Driver function works. For example '
                                         'the \'\'ExDriver\'\' driver is used, which has several modes of operation,'
                                         'which will act further.')
    Moko.Messenger('set', 'set', 'The \'\'set\'\' mode sets a specific command to the driver. This ExDriver driver has'
                                 'the only command is \'\'text\'\'. '
                                 'The result of the \'\'text\'\' command is an empty window with two'
                                 'buttons: \'\'OK\'\' and \'\'Cancel\'\'. Pressing any of them will close the window.')
    Moko.Driver('ExDriver', 'set', 'text')
    Moko.Messenger('set', 'get', 'The \'\'get\'\' mode returns a value of type \'\'boolean\'\'. '
                                 'Pressing on \'\'OK\'\' returns the value'
                                 'True, with \'\'Cancel\'\' - False.')
    resp = Moko.Driver('ExDriver', 'get', 'text', 'boolean')
    if resp:
        Moko.Messenger('set', 'True', 'You clicked on the \'\'OK\'\' button.')
        Moko.Report("exdriver", 'set', 'string', 'You clicked on \'\'OK\'\' and ExDriver returned True.')
    else:
        Moko.Messenger('set', 'False', 'You clicked on the \'\'Cancel\'\' button.')
        Moko.Report("exdriver", 'set', 'string', 'You clicked \'\'Cancel\'\' and ExDriver returned False.')
    Moko.Messenger('set', 'init', 'В режиме \'\'init\'\' на экране появляется окно инициализации драйвера. '
                                  'Так как прибора нет, следует нажать на кнопку \'\'Cancel\'\'.')
    Moko.Driver('ExDriver', 'init', '')
    Moko.Messenger('set', 'command', 'The \'\'text\'\' command has the ability to pass any information to the popup '
                                     'window. For example, we want to display a welcome window. '
                                     'To do this, write \'\'text = Hello, World!\'\'. ')
    Moko.Driver('ExDriver', 'set', 'text=Hello, World!')
    Moko.Report("exdriver_1", 'set', 'string', 'The script completed successfully.')

elif language == 'Русский':
    Moko.Stage('*Driver*', 'Driver')
    Moko.Messenger('set', 'Driver_info', 'В этом скрипте описывается принцип работы функции Driver. Для примера '
                                     'используется драйвер \'\'ExDriver\'\', имеющий несколько режимов работы, '
                                     'которые будут продемонстрированы далее.')
    Moko.Messenger('set', 'set', 'Режим \'\'set\'\' задает определенную команду в драйвер. Данный драйвер \'\'ExDriver\'\' имеет '
                             'единственную команду - \'\'text\'\'. Результатом команды \'\'text\'\' является пустое окно с двумя '
                             'конпками: \'\'OK\'\' и \'\'Cancel\'\'. Нажатие любой из них приведёт к закрытию окна.')
    Moko.Driver('ExDriver', 'set', 'text')

    Moko.Messenger('set', 'get', 'Режим \'\'get\'\' возвращает значение типа \'\'boolean\'\'. При нажатии на \'\'OK\'\' возвращает значение '
                             'True, при \'\'Cancel\'\' - False.')
    resp = Moko.Driver('ExDriver', 'get', 'text', 'boolean')
    if resp:
        Moko.Messenger('set', 'True', 'Вы нажали на кнопку \'\'OK\'\'.')
        Moko.Report("exdriver", 'set', 'string', 'Вы нажали на \'\'OK\'\' и ExDriver вернул значение True.')
    else:
        Moko.Messenger('set', 'False', 'Вы нажали на кнопку \'\'Cancel\'\'.')
        Moko.Report("exdriver", 'set', 'string', 'Вы нажали на \'\'Cancel\'\' и ExDriver вернул значение False.')
        Moko.Messenger('set', 'init', 'В режиме \'\'init\'\' на экране появляется окно инициализации драйвера. Так как прибора нет, '
                              'следует нажать на кнопку \'\'Cancel\'\'.')
        Moko.Driver('ExDriver', 'init', '')

        Moko.Messenger('set', 'command', 'Команда \'\'text\'\' имеет возможность передать какую-либо информацию во всплывающее '
                                 'окно. Например, мы хотим вывести окно с приветствием. '+
               'Для этого в скрипте надо записать \'\'text=Hello,World!\'\'. ')
        Moko.Driver('ExDriver', 'set', 'text=Hello, World!')

        Moko.Report("exdriver_1", 'set', 'string', 'Скрипт успешно завершён.')


Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript('passed')