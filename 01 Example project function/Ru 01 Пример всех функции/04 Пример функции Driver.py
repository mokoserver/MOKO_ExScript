import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('Новый SCRIPT'))
Moko.Stage(stars('*'))

Moko.Stage('*Driver*', 'Driver')
Moko.Messenger('set', 'Driver_info', 'В этом скрипте описывается принцип работы функции Driver. Для примера '
                                 'используется драйвер \'\'ExDriver\'\', имеющий несколько режимов работы, '
                                 'которые будут продемонстрированы далее.')

Moko.Messenger('set', 'set', 'Режим \'\'set\'\' задает определенную команду в драйвер. Данный драйвер \'\'ExDriver\'\' имеет '
                         'команду - \'\'value\'\'. Таким образом Вы можете ввести значение value в драйвер.')
value = Moko.Driver('ExDriver', 'get', 'value', 'string')
Moko.Messenger('set', 'True', f'Вы ввели {value}.')
Moko.Report("exdriver", 'set', 'string', f'Вы ввели {value}.')

Moko.Messenger('set', 'init', 'В режиме \'\'init\'\' на экране появляется окно инициализации драйвера. Так как прибора нет, '
                          'следует нажать на кнопку \'\'Cancel\'\'.')
Moko.Driver('ExDriver', 'init', '')
Moko.Report("exdriver_1", 'set', 'string', 'Скрипт успешно завершён.')


Moko.Stage(stars('*'))
Moko.Stage(stars('Новый SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript('passed')
