'''     Данная библиотека функций служит для осуществления HTTP запросов на MOKO SE.

        26.02.2021 Библиотека переименована в MOKO для удобства разработчиков

        Версия библиотеки: 1.5 от 23.06.2021. Изменен формат post-запросов для драйверов.

        Версия документации: 1.2 от 03.02.2020.
        
        Версия изменена 24.01.2022 для корректной работы старта/паузы/стопа

        Версия изменена 22.08.2022 для обновления функции парсинга и для переноса повторяющегося кода в функции

        Версия изменена 09.09.2022. В формате json параметр type заменен на mode (кроме Stage), поэтому все старые проекты не будут
                                    работать с новой библиотекой, обратной совместимости нет.
 
        Для работы этой библиотеки требуются библиотеки **requests** и **json**.

'''

import requests
from time import sleep
import json
import sys

requests = requests.Session()

_UrlStageWrite: str = 'http://localhost:55001/MOKOSE/stage/stagewrite'

_UrlDriverWrite: str = 'http://localhost:55001/MOKOSE/system/driverwrite'
_UrlDriverRead: str = 'http://localhost:55001/MOKOSE/system/driverread'

_UrlPluginWrite: str = 'http://localhost:55001/MOKOSE/system/pluginwrite'
_UrlPluginRead: str = 'http://localhost:55001/MOKOSE/system/pluginread'

_UrlMessengerWrite: str = 'http://localhost:55001/MOKOSE/system/messengerwrite'
_UrlMessengerRead: str = 'http://localhost:55001/MOKOSE/system/messengerread'

_UrlReportWrite: str = 'http://localhost:55001/MOKOSE/system/reportwrite'
_UrlReportRead: str = 'http://localhost:55001/MOKOSE/system/reportread'

_UrlProgramWrite: str = 'http://localhost:55001/MOKOSE/system/programwrite'
_UrlProgramRead: str = 'http://localhost:55001/MOKOSE/system/programread'

_UrlUtilityWrite: str = 'http://localhost:55001/MOKOSE/system/utilitywrite'
_UrlUtilityRead: str = 'http://localhost:55001/MOKOSE/system/utilityread'

_UrlTelegramWrite: str = 'http://localhost:55001/MOKOSE/system/telegramwrite'
_UrlTelegramRead: str = 'http://localhost:55001/MOKOSE/system/telegramread'

_UrlProjectStateRead: str = 'http://localhost:55001/MOKOSE/status/projectstate'


###################################################################################################################

    ##          ##          ####        ##########      ##        ##     
    ####      ####         ##  ##           ##          ####      ##
    ## ##    ## ##        ##    ##          ##          ## ##     ##
    ##  ##  ##  ##       ##      ##         ##          ##  ##    ##
    ##   ####   ##      ############        ##          ##   ##   ##
    ##    ##    ##      ##        ##        ##          ##    ##  ##
    ##          ##      ##        ##        ##          ##     ## ##
    ##          ##      ##        ##        ##          ##      ####
    ##          ##      ##        ##    ##########      ##       ###

###################################################################################################################


###################################################################################################################

    ##########      ##################          ####     
    ##                      ##                 ##  ##
    ##                      ##                ##    ##  
    ##                      ##               ##      ## 
    ##########              ##              ############
            ##              ##              ##        ##
            ##              ##              ##        ##
            ##              ##              ##        ##
    ##########              ##              ##        ##          

###################################################################################################################


def Stage(stage_string: str, type: str = 'info') -> None:
    """ 
        Функция осуществляет запись строки в Stage.

        :param str stage_string: Строка, записываемая в Stage.
        :param str type: Тип строки в Stage (**Info**, **Error**, **Plugin**, **Driver**, **Report**, **Warning**). По умолчанию **Info**.
        :return: None
        :rtype: *int*

        **Пример:**

        **1.**
        Нам нужно записать строку **'Hello, World!'** в Stage. Для этого напишем следующую команду:

        >>> Stage('Hello, World!')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"string": "Hello World!", "type":"info"}'``

        В Stage программы MOKO SE должна появиться информационная строка:

        ``Hello World!``

        Функция должна вернуть следующее значение:

        ``200``

        Иначе не выполняется либо возвращает код состояния HTTP запроса. Например:

        ``400``

        А в терминале:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        **2.**
        Нам нужно записать строку ошибки **'ERROR! Wrong request type!'** в Stage.

        Если мы указываем тип выводимой строки, то команда будет иметь следующий вид:

        >>> Stage('ERROR! Wrong request type!', 'ERROR')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"string": "ERROR IN PYTHON LIBRARY! Wrong request type!", "type":"ERROR"}'``

        В Stage программы MOKO SE должна появиться строка ошибки:

        ``ERROR! Wrong request type!``

        А также функция должна вернуть следующее значение:

        ``200``

        Иначе не выполняется либо возвращает код состояния HTTP запроса. Например:

        ``404``

        А в терминале:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    '+str(name)+'
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза

    URLWrite: str = _UrlStageWrite
    command_to_send: str = '{"string" :"'+str(stage_string)+'", "type":"'+str(type)+'"}'
    send_request(URLWrite, command_to_send)


###################################################################################################################

    #####           #######         ##########
    ##   ##         ##     ##           ##
    ##     ##       ##      ##          ##    
    ##      ##      ##     ##           ##    
    ##      ##      #######             ##
    ##      ##      ####                ##
    ##     ##       ## ##               ##
    ##   ##         ##   ##             ##
    #####           ##     ##       ##########

###################################################################################################################


def Driver(name: str, mode: str, command: str, valuetype: str = 'void') -> ...:
    """ 
        Функция осуществляет работу с драйвером.

        :param str name: Имя драйвера
        :param str mode: Тип команды (**'get'**, **'set'**, **'init'**, **'close'**)
        :param str command: Команда, которую записывает драйвер в управляемый прибор
        :param str valuetype: **(только для mode = 'get')** Тип данных, получаемых из драйвера. По умолчанию *void*.
        :return: Функция возвращает *None* (если mode = **'set'**) либо принятые с драйвера данные (если mode = **'get'**)
        :rtype: Возвращаемый тип данных меняется в зависимости от полученных из драйвера значений

        **Пример:**

        **1.**
        Нам нужно проиницилизировать драйвер прибора SMBV100A. Для этого напишем следующую команду:

        >>> Driver('SMBV100A', 'init', '')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"name": "SMBV100A", "mode": "init", "command": ""}'``

        На экране должно появиться окно инициализации драйвера(выбор интерфейса).

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        **2.**
        Нам нужно сбросить прибор SMBV100A. Для этого напишем следующую команду:

        >>> Driver('SMBV100A', 'set', 'reset')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"name": "SMBV100A", "mode": "set", "command": "reset"}'``

        Драйвер должен сбросить настройки прибора SMBV100A.

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        **3.**
        Нам нужно прочитать значение тестового окошка тестового драйвера. Для этого напишем следующую команду:

        >>> Driver('Test', 'get', 'test', 'bool')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"name": "Test", "mode": "get", "command": "test"}'``

        На экране должно отобразиться окно с надписью 'Test' и двумя кнопками 'OK' и 'Cancel'.

        В зависимости от нажатой кнопки драйвер и функция должны вернуть:

        ``True('OK') либо False('Cancel').``

        В случае какой-либо ошибки функция не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        А если не ввести `valuetype`, то функция не отработает, о чём оповестит в терминале и Stage программы MOKO SE.
    """

    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set", "init", "close", "check"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None

    URLWrite: str = _UrlDriverWrite
    URLRead: str = _UrlDriverRead

    command_to_send: str = '{"name":"' + str(name) + '","mode":"' + str(mode) + '","command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    drvdata: str = check_status("driver", mode, URLRead)
    return parse_data(drvdata, mode, valuetype)


###################################################################################################################

    #######         ##                  ##         ##
    ##     ##       ##                  ##         ##
    ##      ##      ##                  ##         ##
    ##     ##       ##                  ##         ##
    #######         ##                  ##         ##
    ##              ##                  ##         ##
    ##              ##                  ##         ##
    ##              ##                  ##         ##
    ##              #############       #############         

###################################################################################################################


def Plugin(name: str, mode: str, command: str, valuetype: str = 'void') -> ...:

    """ 
        Функция осуществляет работу с плагином.

        :param str name: Имя плагина
        :param str mode: Тип команды (**'get'**, **'set'**, **'init'**)
        :param str command: Команда, которую отправляем в плагин.
        :param str valuetype: (только для mode = **'get'**) Тип данных, получаемых из плагина. По умолчанию *void*.
        :return: Функция возвращает *None* (если mode = **'set'**) либо принятые с плагина данные (если mode = **'get'**)
        :rtype: Возвращаемый тип данных меняется в зависимости от полученных из плагина значений

        **Пример:**

        **1.**
        Нам нужно проинициализировать плагин NMEA0183. Для этого напишем следующую команду:

        >>> Plugin("NMEA0183", "init", "")

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"name": "NMEA0183", "mode": "init", "command": ""}'``

        На экране должно появиться окно плагина.

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        **2.**
        Нам нужно сбросить протоколы плагина NMEA0183. Для этого напишем следующую команду:

        >>> Plugin("NMEA0183", "set", "ProtocolReset=True")

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"name": "NMEA0183", "mode": "set", "command": "ProtocolReset=True"}'``

        Плагин NMEA0183 должен сбросить протоколы.

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        **3.**
        Нам нужно прочитать время определения координат из плагина NMEA0183. Для этого напишем следующую команду:

        >>> Plugin('NMEA0183', 'get','CoordinatesValidTime', 'float')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"name": "NMEA0183", "mode": "get", "command": "CoordinatesValidTime"}'``

        Функция должна вернуть следующее значение некоторое время в секундах:

        ``0 (но для данной команды плагина NMEA0183 это признак ошибки при работе)``

        либо, например:

        ``17.56``

        В случае какой-либо ошибки функция не выполняется, либо отображает какую-то ошибку, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        А если не ввести *valuetype*, то функция не отработает, о чём оповестит в терминале и Stage программы MOKO SE.

    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set", "init", "close"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None

    URLWrite: str = _UrlPluginWrite
    URLRead: str = _UrlPluginRead

    command_to_send: str = '{"name":"' + str(name) + '","mode":"' + str(mode) + '","command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    plgdata: str = check_status("plugin", mode, URLRead)
    return parse_data(plgdata, mode, valuetype)


###################################################################################################################

    ##          ##      ############        ##########
    ####      ####      ##                  ##        
    ## ##    ## ##      ##                  ##        
    ##  ##  ##  ##      ##                  ##        
    ##   ####   ##      ########            ##########
    ##    ##    ##      ##                          ##
    ##          ##      ##                          ##
    ##          ##      ##                          ##
    ##          ##      ############        ##########

###################################################################################################################


def Messenger(mode: str, head: str, body: str, valuetype: str = 'void', delaytime: str = 'void') -> ...:
    """ 
        Функция осуществляет появление на экране всплывающего сообщения с опциональным полем для ввода данных

        :param str mode: Тип команды (**'get'**, **'set'**)
        :param str head: Заголовок сообщения.
        :param str body: Содержание сообщения.
        :param str valuetype: **(только для mode = 'get')** Тип данных, получаемых из сообщения. По умолчанию *void*.
        :param str delaytime: *(если необходимо)* Время задержки в секундах.
        :return: Функция возвращает *None* (если mode = **'set'**) либо введённые в окне сообщения данные (если mode = **'get'**)
        :rtype: Возвращаемый тип данных меняется в зависимости от полученных из сообщения значений

        **Пример:**

        **1.**
        Нам нужно отобразить сообщение для пользователя, которое просит присоединить прибор и запустить плагин NMEA0183. Для этого напишем следующую команду:

        >>> Messenger('set', 'Info', 'Please connect the device and launch NMEA0183 plugin.')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"mode": "set", "head": "Info", "body": "Please connect the device and launch NMEA0183 plugin."}'``

        На экране должно появиться окно с сообщением, в котором в заголовке будет написано 'Info', а в теле - 'Please connect the device and launch NMEA0183 plugin.'.

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        **2.**
        Нам нужно отобразить сообщение для пользователя, чтобы он ввёл некоторое число. Для этого напишем следующую команду:

        >>> Messenger('get', 'First number', 'Please, enter the first number', 'int')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"mode": "get", "head": "First number", "body": "Please, enter the first number"}'``

        На экране должно появиться окно с сообщением, в котором в заголовке будет написано 'First number', а в теле - 'Please, enter the first number.'. Также это сообщение будет иметь поле для ввода данных.

        Функция должна вернуть введённое число, например:

        ``123``

        Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        А если не ввести *valuetype*, то функция не отработает, о чём оповестит в терминале и Stage программы MOKO SE.

        **3.**
        Нам нужно отобразить сообщение о задержке выполнения скрипта на 15 минут.

        Если нам необходима задержка в сообщении, то это делается как в следующем примере:

        >>> MOKO.Messenger('set', 'Info', 'Please, wait for 15 minutes', 'void', str(15*60))

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"mode": "set", "head": "Info", "body": "Please, wait for 15 minutes", "time": "900"}'``

        На экране должно появиться окно с сообщением, в котором в заголовке будет написано 'Info', а в теле - 'Please, wait for 15 minutes.'.

        Также должен появиться таймер, отсчитывающий 15 минут.

        В случае какой-либо ошибки функция не выполняется, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None

    URLWrite: str = _UrlMessengerWrite
    URLRead: str = _UrlMessengerRead
    
    if (delaytime == 'void'):
        command_to_send: str = '{"mode":"'+str(mode)+'","head":"'+str(head)+'","body":"'+str(body)+'","value":"'+str(valuetype)+'"}'
    else:
        command_to_send: str = '{"mode":"'+str(mode)+'","head":"'+str(head)+'","body":"'+str(body)+'","time":"'+str(delaytime)+'"}'

    send_request(URLWrite, command_to_send)

    msgdata: str = check_status("messenger", mode, URLRead)
    return parse_data(msgdata, mode, valuetype)


###################################################################################################################

    ######          ############        #######
    ##    ##        ##                  ##     ##
    ##     ##       ##                  ##      ##
    ##   ##         ##                  ##     ##
    ## ##           ######              ####### 
    ####            ##                  ##
    ## ##           ##                  ##
    ##   ##         ##                  ##
    ##     ##       ############        ##

###################################################################################################################


def Report(name: str, mode: str, kind: str, data: str, valuetype: str = 'void') -> ...:
    """ 
        Функция осуществляет работу с данными в отчёте.

        :param str name: Название для записываемых в отчёт данных и имя закладки в документе-шаблоне Word
        :param str mode: Тип команды (пока что только **'set'**)
        :param str kind: В каком виде данные записываются в отчёт(**string** - строка и **table** - таблица)
        :param str data: Записываемые в отчёт данные
        :param str valuetype: (только для mode = 'get') Тип данных, получаемых из отчёта. По умолчанию *void*.
        :return: Функция возвращает *None* (если mode = **'set'**) либо полученные из отчёта данные (если mode = **'get'**)
        :rtype: Возвращаемый тип данных меняется в зависимости от полученных из отчёта значений

        **Пример:**

        **1.**
        Нам нужно вывести строку *'FgsFds'* в отчёт. Для этого напишем следующую команду:

        >>> Report("rep1",'set', 'string', 'FgsFds')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"name": "rep1", "mode": "set", "kind": "string", "data": "FgsFds"}'``

        В программе MOKO SE во вкладке 'Report' в таблице 'Report names' должен появиться элемент 'rep1'. По нажатию на этот элемент в таблице 'Reports' должна появиться строка *FgsFds*.

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

        **2.**
        Нам нужно вывести 3 строки в таблицу отчёта. Для этого напишем следующую команду:

        >>> Report("rep2",'set', 'table', 'FgsFds, fgsfds, etc')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"name": "rep2", "mode": "set", "kind": "table", "data": "FgsFds, fgsfds, etc"}'``

        В программе MOKO SE во вкладке 'Report' в таблице 'Report names' должен появиться элемент 'rep2'. По нажатию на этот элемент в таблице 'Reports' три столбца в одной строке должны заполниться значениями соответственно 'FgsFds', 'fgsfds' и 'etc'.

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``
    
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set", "info", "clear", "delete", "save"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None
    if ((kind.lower() != 'table') and (kind.lower() != 'string') and (kind.lower() != 'picture') and (kind.lower() != 'strings')):
        Stage("ERROR IN PYTHON LIBRARY! WRONG REPORT KIND! " + str(kind), 'error')
        print("ERROR IN PYTHON LIBRARY! WRONG REPORT KIND! " + str(kind))
        return None

    URLWrite: str = _UrlReportWrite
    URLRead: str = _UrlReportRead
    
    command_to_send: str = '{"name":"'+str(name)+'","mode":"'+str(mode)+'", "kind":"'+str(kind)+'", "data":"'+str(data)+'"}'
    send_request(URLWrite, command_to_send)

    repdata: str = check_status("report", mode, URLRead)
    return parse_data(repdata, mode, valuetype)


###################################################################################################################

    ##         ##   ##################      
    ##         ##           ##          
    ##         ##           ##          
    ##         ##           ##  
    ##         ##           ##
    ##         ##           ##
    ##         ##           ##
    ##         ##           ##
    #############           ##

###################################################################################################################


def Utility(name: str, mode: str, command: str, valuetype: str = 'void') -> ...:

    """ 
        Функция осуществляет работу с утилитой.

        :param str name: Имя утилиты
        :param str mode: Тип команды (**'get'**, **'set'**)
        :param str command: Команда, которую отправляем в утилиту.
        :param str valuetype: (только для mode = **'get'**) Тип данных, получаемых из утилиты. По умолчанию *void*.
        :return: Функция возвращает *None* (если mode = **'set'**) либо принятые с утилиты данные (если mode = **'get'**)
        :rtype: Возвращаемый тип данных меняется в зависимости от полученных из утилиты значений
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set", "init", "check"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None

    URLWrite: str = _UrlUtilityWrite
    URLRead: str = _UrlUtilityRead

    command_to_send: str = '{"name" :"' + str(name) + '", "mode":"' + str(mode) + '", "command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    utldata: str = check_status("utility", mode, URLRead)
    return parse_data(utldata, mode, valuetype)


###################################################################################################################

    #######         ######          #############
    ##     ##       ##    ##        ##         ##
    ##      ##      ##     ##       ##         ##
    ##     ##       ##   ##         ##         ##
    #######         ## ##           ##         ##
    ##              ####            ##         ##
    ##              ## ##           ##         ##
    ##              ##   ##         ##         ##
    ##              ##     ##       #############

###################################################################################################################    


def Program(name: str, mode: str, command: str, valuetype: str = 'void') -> ...:
    """ 
        Функция осуществляет управление программой MOKO SE (скриптами, проектами и т.д.)

        :param str name: название типа, которым нужно управлять ('script', 'project', etc.)
        :param str mode: тип команды (пока что только **'set'**).
        :param str command: Команда, которую посылаем в MOKO SE.
        :param str valuetype: (только для mode = 'get') Тип возвращаемых данных. По умолчанию *void*.
        :return: Функция возвращает *None* (если mode = **'set'**) либо полученные данные (если mode = **'get'**)
        :rtype: Возвращаемый тип данных меняется в зависимости от полученных из отчёта значений

        **Пример:**

        **1.**
        Нам нужно дать серверу знать, что скрипт окончен. для этого напишем следующую команду:

        >>> Program('script', 'set', 'done')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        b'{"name": "script", "mode": "set", "command": "done"}'

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set", "init", "close"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None

    URLWrite: str = _UrlProgramWrite
    URLRead: str = _UrlProgramRead

    command_to_send: str = '{"name":"' + str(name) + '","mode":"' + str(mode) + '","command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    progdata: str = check_status("program", mode, URLRead)
    return parse_data(progdata, mode, valuetype)

def EndScript(command: str = 'done') -> None:
    """ 
        Обязательная функция, которая должна быть в конце каждого скрипта. Даёт знать серверу, что скрипт закончен.
    """
    Program('script','set',command)
    sys.exit()


###################################################################################################################

    ####################    #############    ##
             ##             ##               ##
             ##             ##               ##
             ##             ##               ##
             ##             ########         ##
             ##             ##               ##
             ##             ##               ##
             ##             ##               ##
             ##             #############    #############

###################################################################################################################


def Telegram(role: str, mode: str, command: str, valuetype: str = 'void') -> ...:
    """
        Функция осуществляет работу с Telegram.

        :param str role: ####################################
        :param str mode: Тип команды (**'get'**, **'set'**)
        :param str command: Команда, которая передается в Telegram
        :return: Функция возвращает *None* (если mode = **'set'**) либо принятые с Telegram данные (если mode = **'get'**)
        :rtype: Возвращаемый тип данных меняется в зависимости от полученных из драйвера значений

        **Пример:**

        **1.**
        Мы хотим, чтобы Telegram-бот передал нам введенное сообщение. Для этого напишем следующую команду:

        >>> Telegram('alpha', 'set', 'Hello, I\\'m a bot!')

        В случае успешного выполнения в терминале должна появиться следующая строка:

        ``b'{"role": "alpha", "mode": "set", "command": "Hello, I'm a bot!"}'``

        Вас придет сообщение в Telegram.

        Функция должна вернуть следующее значение:

        ``None``

        Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

        ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None

    URLWrite: str = _UrlTelegramWrite
    URLRead: str = _UrlTelegramRead

    command_to_send: str = '{"role":"' + str(role) + '","mode":"' + str(mode) + '","command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    tgmdata: str = check_status("telegram", mode, URLRead)
    return parse_data(tgmdata, mode, valuetype)


###################################################################################################################

    ##        ##    ############    ##              ######
    ##        ##    ##              ##              ##    ##
    ##        ##    ##              ##              ##    ##
    ##        ##    ##              ##              ##  ##
    ############    ######          ##              ####
    ##        ##    ##              ##              ##
    ##        ##    ##              ##              ##
    ##        ##    ##              ##              ##
    ##        ##    ############    #############   ##        

###################################################################################################################


def project_state() -> None:
    """
        project_state - предназначена для проверки старта/паузы/стопа
    """
    URLPSRead: str = _UrlProjectStateRead
    serverstate = requests.get(URLPSRead)
    JSONprojectstate = json.loads(serverstate.content)
    projectstate: str = JSONprojectstate.get('projectstate')
    while (projectstate.lower() != 'run'):
        sleep(0.05)
        serverstate = requests.get(URLPSRead)
        JSONprojectstate = json.loads(serverstate.content)
        projectstate: str = JSONprojectstate.get('projectstate')
        if (projectstate.lower() == 'stop'):
            sys.exit()

def check_status(system: str, mode: str, URLRead: str) -> str:
    """
        check_status - предназначена для проверки статуса MOKO SE (ready или busy),
        а также для проверки status_code (если более 9 раз плохо приняты данные, то выдаем ошибку).

        :param str system: функция, которая вызывает (Driver, Program, ...)
        :param str mode: тип команды ('get', 'set', 'init', 'close', ...)
        :param str URLRead: URL для получения данных от сервера
        :return: Функция возвращает данные от сервера. Если badresponse > 9, то возвращается пустая строка (False)
    """
    data: str = ""
    timeout: int = 0
    badresponse: int = 0
    status: str = "none"
    while ((status.lower() != 'ready') and (badresponse < 10)):
        response = requests.get(URLRead)
        # Проверка состояния проекта: Старт/Стоп/Пауза
        project_state()
        if (response.status_code != 200):
            Stage("ERROR IN PYTHON LIBRARY! BAD RESPONSE CODE! " + str(response.status_code), 'error')
            print("ERROR IN PYTHON LIBRARY! BAD RESPONSE CODE! " + str(response.status_code) + '\n' +
                  str(10 - badresponse) + ' TRIES LEFT')
            badresponse += 1
        else:
            y = json.loads(response.content)
            status: str = y.get(f'{system}status')
            if (mode.lower() == 'get' or 'check'):
                data: str = y.get(f'{system}data')
            timeout += 1
        sleep(0.05)

    if is_bad_response(badresponse): return ""
    return data

def parse_data(data: str, mode: str, valuetype: str = 'void') -> ...:
    """
        parse_data - парсинг полученных данных в зависимости от переданного valuetype.

        :param str data: полученные данные
        :param str mode: тип команды ('get', 'set', 'init', 'close', ...)
        :param str valuetype: тип возвращаемых данных (только при mode = "get")
        :return: Функция возвращает данные того типа, который был указан в valuetype
    """
    if mode.lower() not in ["get", "check"]: return None

    splitter: str = ";"
    if is_semicolon_error(data, splitter, valuetype): return None

    data: str = check_data(data, splitter)

    if valuetype.lower() == 'boolean':
        data: str = data.split(splitter)[0]
        return True if data.lower() == "true" else False
    elif valuetype.lower() == 'float':
        data: str = data.split(splitter)[0]
        return float(data.replace(",", "."))
    elif valuetype.lower() == 'int':
        data: str = data.split(splitter)[0]
        data: str = data.split(".")[0]
        return int(data.split(",")[0])
    elif valuetype.lower() == 'arrayboolean':
        return to_list(bool, data, splitter)
    elif valuetype.lower() == 'arrayfloat':
        return to_list(float, data, splitter)
    elif valuetype.lower() == 'arrayint':
        return to_list(int, data, splitter)
    elif valuetype.lower() == 'arraystring':
        return to_list(str, data, splitter)
    else: # Используется в качестве valuetype = 'string'
        return data.split(splitter)[0]

def check_data(data: str, splitter: str = ";") -> str:
    """
        check_data - предназначена для проверки полученных данных. Если есть символ ";" в конце полученных данных, то он
                     удаляется

        :param str data: полученные данные
        :param str splitter: символ, по которому идет разбиение данных
        :return: Функция возвращает проверенные данные
    """
    if data.rfind(splitter) == len(data)-1:
        data: str = data[:-1]
    return data

def to_list(func, data: str, splitter: str = ";") -> ...:
    """
        to_list - предназначена для разбиения входных данных с последующим занесением в список

        :param func: функция, которая применяется к данным (int(), float(), ...)
        :param str data: полученные данные
        :param str splitter: символ, по которому идет разбиение данных
        :return: Функция возвращает список, содержащий значения типа, соответствующих типу func() => (int, float, ...)
    """
    split_data: list = data.split(splitter)
    result: list = []
    for spl in split_data:
        if func is bool:
            result.append(True if spl.lower() == "true" else False)
        elif func is int:
            spl: str = spl.split(".")[0]
            result.append(func(spl.split(",")[0]))
        elif func is float:
            result.append(func(spl.replace(",", ".")))
        else:
            result.append(func(spl))
    return result

def is_semicolon_error(data: str, splitter: str, valuetype: str) -> bool:
    """
        is_semicolon_error - проверяет наличие двух символов splitter в конце входных данных.

        :param str data: полученные данные
        :param str splitter: символ, по которому идет разбиение
        :param str valuetype: - тип возвращаемых данных (только при mode = "get")
        :return: Функция печатает ошибку в консоль и в Stage программы MOKO SE, если в конце два символа splitter.
                 Если ошибка - возвращает True, иначе - False

        Например, если splitter = ";", а data = "123;;", то будет ошибка.
    """
    if data[-2:] == f"{2*splitter}":
        Stage(f'ERROR IN PYTHON LIBRARY!','error')
        Stage(f'INPUT DATA CONTAINS MORE THAN 1 \'\'{splitter}\'\' AT THE END!', 'error')
        Stage(f'DATA: {data}     =>     VALUETYPE: {valuetype.upper()}', 'error')
        print(f'ERROR IN PYTHON LIBRARY!')
        print(f'INPUT DATA CONTAINS MORE THAN 1 \'\'{splitter}\'\' AT THE END!')
        print(f'DATA: {data}     =>     VALUETYPE: {valuetype.upper()}')
        return True
    return False

def is_bad_response(badresponse: int) -> bool:
    """
        is_bad_response - предназначена для проверки ответов сервера.
        Если больше 9 ответов сервера были "плохими", то функция возвращает True, иначе - False

        :param int badresponse: количество "плохих" ответов сервера
        :return: Функция печатает ошибку в консоль и в Stage программы MOKO SE, если количество "плохих" ответов больше 9.
                 Если ошибка - возвращает True, иначе - False
    """
    if (badresponse >= 10):
        Stage("ERROR IN PYTHON LIBRARY! FUNCTION EXIT BECAUSE OF BAD RESPONSES", 'error')
        print("ERROR IN PYTHON LIBRARY! FUNCTION EXIT BECAUSE OF BAD RESPONSES")
        return True
    return False

def is_mode_and_valuetype_incorrect(mode: str, valuetype: str) -> bool:
    """
        is_mode_and_valuetype_incorrect - предназначена для проверки mode и valuetype.
        Если mode = get, а valuetype = void - ошибка

        :param str mode: тип команды ('get', 'set', 'init', 'close', ...)
        :param str valuetype: тип возвращаемых данных (только при mode = "get")
        :return: Функция печатает ошибку в консоль и в Stage программы MOKO SE, если при mode = "get", valuetype = "void" или "".
                 Если ошибка - возвращает True, иначе - False
    """
    if (mode.lower() == 'get') and (valuetype.lower() == 'void' or valuetype.lower() == ''):
        Stage("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request", 'error')
        print("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request")
        return True
    return False

def is_mode_incorrect(mode: str, modes_list:list) -> bool:
    """
        is_mode_correct - предназначена для проверки значения mode: корректное либо нет.

        :param str mode: тип команды ('get', 'set', 'init', 'close', ...)
        :param list modes_list: список mode, который корректен для данной функции (Driver, Program,...)
        :return: Функция печатает ошибку в консоль и в Stage программы MOKO SE, если в modes_list нет указанного mode.
                 Если ошибка - возвращает True, иначе - False
    """
    if mode.lower() not in modes_list:
        Stage("ERROR IN PYTHON LIBRARY! Wrong request mode! " + str(mode), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong request mode! " + str(mode))
        return True
    return False

def send_request(URLWrite: str, command_to_send: str) -> None:
    """
        send_request - предназначена для отсылки команды/запроса на сервер

        :param str URLWrite: адрес сервера, для отправки команды/запроса
        :param command_to_send: команда/запрос, отправляемый на сервер в формате json
        :return: Функция возвращает None
    """
    headers: dict = {'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(URLWrite, headers=headers, data=command_to_send.encode('utf-8'))
    print(response.content)