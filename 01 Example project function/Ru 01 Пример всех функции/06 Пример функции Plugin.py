import MOKO as Moko
from MOSC import stars
import time

Moko.Stage(stars('*'))
Moko.Stage(stars('Новый SCRIPT'))
Moko.Stage(stars('*'))
language = Moko.Report("language", 'get', 'string', 'string', 'string')

Moko.Plugin('ExPlugin', 'init', '')

time.sleep(5)

Moko.Stage('*Plugin*', 'Plugin')
Moko.Messenger('set', 'Plugin_info', 'В это скрипте описывается принцип работы функции Plugin. Для примера '
                                 'используется плагин \'\'ExPlugin\'\', имеющий 2 режима работы: \'\'set\'\' и \'\'get\'\'.')
Moko.Messenger('set', 'Set Number1|2', 'Команда \'\'Number1|2\'\' задает число Number1 или Number2 в окне Main. Для этого '
                                   'после команды ставиться = и число, которое нужно записать. ' +
           'По умолчанию числа Number1 и Number2 равны нулю.')
Moko.Plugin('ExPlugin', 'set', 'Number1=9')
Moko.Plugin('ExPlugin', 'set', 'Number2=14')
Moko.Messenger('set', 'Get Sum', 'Команда \'\'Sum\'\' возвращает сумму из поля Sum в окне Main.')
sum = Moko.Plugin('ExPlugin', 'get', 'Sum', 'string')
Moko.Messenger('set', 'Sum', 'Сумма: ' + sum)
Moko.Report("explugin_1", 'set', 'string', sum)

Moko.Messenger('set', 'Set String', 'Команда \'\'Set String\'\' записывает какую-либо строку в ExPlugin. Для этого после '
                                'команды ставиться = и информация, которую нужно записать. ' +
           'Информация отобразится в поле String в окне Main.')
Moko.Plugin('ExPlugin', 'set', 'String=Hello, World!')
Moko.Messenger('set', 'Get String', 'Команда \'\'Get String\'\' возвращает строку из поля String в окне Main.')
a = Moko.Plugin('ExPlugin', 'get', 'String', 'string')
Moko.Messenger('set', 'String', 'Строка из ExPlugin: ' + a)
Moko.Report("explugin", 'set', 'string', a)

Moko.Messenger('set', 'Set Screenshot', 'Команда \'\'Screenshot\'\' делает скриншот плагина, название которого состоит из '
                                    'даты и времени в момент скриншота. Скриншот сохраняется в отдельную папку '
                                    'App/screenshots в корневом каталоге ExPlugin.')
Moko.Plugin('ExPlugin', 'set', 'Screenshot')
Moko.Messenger('set', 'Set ChangeLedLoop', 'Команда \'\'ChangeLedLoop\'\' меняет значение индикатора Led Loop в окне Main.')
Moko.Plugin('ExPlugin', 'set', 'ChangeLedLoop')

Moko.Messenger('set', 'Set ShowTab', 'Команда \'\'Showtab\'\' меняте отображает нужное окно плагина (Main | Graph | Info). '
                                 'Для этого после команды ставиться = и название нужного окна.')
Moko.Plugin('ExPlugin', 'set', 'ShowTab=Info')
time.sleep(10)
Moko.Plugin('ExPlugin', 'set', 'ShowTab=Graph')
time.sleep(3)
Moko.Messenger('set', 'Set Graph', 'Команда \'\'Graph\'\' запускает или останавливает график в окне Graph. Для старта после '
                               'команды \'\'Graph\'\' ставиться =start, а для остановки =stop.')
Moko.Plugin('ExPlugin', 'set', 'Graph=start')

Moko.Messenger('set', 'Get InstantScreenshot', 'Команда \'\'InstantScreenshot\'\' возвращает скриншот окна ExPlugin.')
screen = Moko.Plugin('ExPlugin', 'get', 'InstantScreenshot', 'string')
Moko.Report("explugin_2", 'set', 'picture', screen)
Moko.Plugin('ExPlugin', 'set', 'Graph=stop')

Moko.Report("explugin_3", 'set', 'string', 'Скрипт успешно завершён.')

Moko.Stage(stars('*'))
Moko.Stage(stars('Следующий SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()
