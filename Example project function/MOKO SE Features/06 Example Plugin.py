import MOKO as Moko
from MOSC import stars
import time

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))
language = Moko.Report("language", 'get', 'string', 'string', 'string')

Moko.Plugin('ExPlugin', 'init', '')

time.sleep(5)

if language == 'English(default)':
    Moko.Stage('*Plugin*', 'Plugin')
    Moko.Messenger('set', 'Plugin_info', 'This script describes how the Plugin function works. For example '
                                         'the plugin \'\'ExPlugin\'\' is used, which has 2 modes of operation: '
                                         '\'\'set\'\' and \'\'get\'\'.')
    Moko.Messenger('set', 'Set Number1|2', 'The \'\'Number1|2\'\' command sets the number to Number1 or Number2 '
                                           'in the Main window. For this after the command = and the number '
                                           'to be written. By default, the numbers Number1 and Number2 are zero.')
    Moko.Plugin('ExPlugin', 'set', 'Number1=9')
    Moko.Plugin('ExPlugin', 'set', 'Number2=14')
    Moko.Messenger('set', 'Get Sum', 'The \'\'Sum\'\' command returns the sum from the Sum field in the Main window.')
    sum = Moko.Plugin('ExPlugin', 'get', 'Sum', 'string')
    Moko.Messenger('set', 'Sum', 'Sum: ' + sum)
    Moko.Report("explugin_1", 'set', 'string', sum)
    Moko.Messenger('set', 'Set String', 'The \'\'Set String\'\' command writes a string to the ExPlugin. To do this, after '
                                        'command is set = and the information to be recorded. '
                                        'The information is displayed in the String field in the Main window.')
    Moko.Plugin('ExPlugin', 'set', 'String=Hello, World!')
    Moko.Messenger('set', 'Get String', 'The Get String command returns a string from the String field '
                                        'in the Main window.')
    a = Moko.Plugin('ExPlugin', 'get', 'String', 'string')
    Moko.Messenger('set', 'String', 'String from ExPlugin: ' + a)
    Moko.Report("explugin", 'set', 'string', a)
    Moko.Messenger('set', 'Set Screenshot', 'The \'\'Screenshot\'\' command takes a screenshot of the plugin, '
                                            'whose name consists of'
                                            'date and time at the moment of the screenshot. '
                                            'The screenshot is saved in a separate folder '
                                            'App/screenshots in ExPlugin root directory')
    Moko.Plugin('ExPlugin', 'set', 'Screenshot')
    Moko.Messenger('set', 'Set ChangeLedLoop', 'The \'\'ChangeLedLoop\'\' command changes the value'
                                               ' of the Led Loop indicator in the main window.')
    Moko.Plugin('ExPlugin', 'set', 'ChangeLedLoop')
    Moko.Messenger('set', 'Set ShowTab', 'The command \'\'Showtab\'\' change displays the desired plugin '
                                         'window (Main | Graph | Info). '
                                         'To do this, after the command, put = and the name of the required window.')
    Moko.Plugin('ExPlugin', 'set', 'ShowTab=Info')
    time.sleep(10)
    Moko.Plugin('ExPlugin', 'set', 'ShowTab=Graph')
    time.sleep(3)
    Moko.Messenger('set', 'Set Graph', 'The \'\'Graph\'\' command starts or stops a graph in the Graph window. '
                                       'To start after command \'\'Graph\'\' is set =start, and for stop =stop.')
    Moko.Plugin('ExPlugin', 'set', 'Graph=start')
    Moko.Messenger('set', 'Get InstantScreenshot', 'The \'\'InstantScreenshot\'\' command returns a screenshot'
                                                   ' of the ExPlugin window.')
    screen = Moko.Plugin('ExPlugin', 'get', 'InstantScreenshot', 'string')
    Moko.Report("explugin_2", 'set', 'picture', screen)
    Moko.Plugin('ExPlugin', 'set', 'Graph=stop')
    Moko.Report("explugin_3", 'set', 'string', 'The script completed successfully.')

elif language == 'Русский':
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
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()