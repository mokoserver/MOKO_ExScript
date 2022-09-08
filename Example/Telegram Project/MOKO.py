'''     Данная библиотека функций служит для осуществления HTTP запросов на MOKO SE.

        26.02.2021 Библиотека переименована в MOKO для удобства разработчиков

        Версия библиотеки: 1.5 от 23.06.2021. Изменен формат post-запросов для драйверов.

        Версия документации: 1.2 от 03.02.2020.
        
        Версия изменена 24.01.2022 для корректной работы старта/паузы/стопа

        Версия изменена 22.08.2022 для обновления функции парсинга и для переноса повторяющегося кода в функции
 
        Для работы этой библиотеки требуются библиотеки **requests** и **json**.

'''

import requests
from time import sleep
import json
import sys

requests = requests.Session()

_UrlStageWrite = 'http://localhost:55001/MOKOSE/stage/stagewrite'

_UrlDriverWrite = 'http://localhost:55001/MOKOSE/system/driverwrite'
_UrlDriverRead = 'http://localhost:55001/MOKOSE/system/driverread'

_UrlPluginWrite = 'http://localhost:55001/MOKOSE/system/pluginwrite'
_UrlPluginRead = 'http://localhost:55001/MOKOSE/system/pluginread'

_UrlMessengerWrite = 'http://localhost:55001/MOKOSE/system/messengerwrite'
_UrlMessengerRead = 'http://localhost:55001/MOKOSE/system/messengerread'

_UrlReportWrite = 'http://localhost:55001/MOKOSE/system/reportwrite'
_UrlReportRead = 'http://localhost:55001/MOKOSE/system/reportread'

_UrlProgramWrite = 'http://localhost:55001/MOKOSE/system/programwrite'
_UrlProgramRead = 'http://localhost:55001/MOKOSE/system/programread'

_UrlUtilityWrite = 'http://localhost:55001/MOKOSE/system/utilitywrite'
_UrlUtilityRead = 'http://localhost:55001/MOKOSE/system/utilityread'

_UrlTelegramWrite = 'http://localhost:55001/MOKOSE/system/telegramwrite'
_UrlTelegramRead = 'http://localhost:55001/MOKOSE/system/telegramread'

_UrlProjectStateRead = 'http://localhost:55001/MOKOSE/status/projectstate'


_Messenger_CurrentType = 0

_Driver_CurrentName = 0
_Driver_CurrentType = 0
_Driver_CurrentCommand = 0

_ReadTimeout = -1


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

# Stage - функция, осуществляющая запись строки в Stage (даёшь рекурсию)
# stage_string - Строка, записываемая в Stage
# type - Тип строки в Stage (Info, Error, Plugin, Driver, Report, Warning). По умолчанию Info.
def Stage(stage_string, type='info'):
    """ 
    Функция осуществляет запись строки в Stage.

    :param str stage_string: Строка, записываемая в Stage.
    :param str type: Тип строки в Stage (**Info**, **Error**, **Plugin**, **Driver**, **Report**, **Warning**). По умолчанию **Info**.
    :return: Функция возвращает код статуса HTTP запроса
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

    URLWrite = _UrlStageWrite
    command_to_send = '{"string" :"'+str(stage_string)+'", "type":"'+str(type)+'"}'
    send_request(URLWrite, command_to_send)

    return None


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

# Driver - функция, осуществляющая работу с драйвером
# name - имя драйвера
# mode - тип команды ('get', 'set', 'init', 'close')
# command - команда, которую записывает драйвер в управляемый прибор
# valuetype (только для type = 'get') - тип данных, получаемый из драйвера. По умолчанию void
def Driver(name, mode, command, valuetype='void'):
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

    ``b'{"name": "SMBV100A", "type": "init", "command": ""}'``

    На экране должно появиться окно инициализации драйвера(выбор интерфейса).

    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **2.**
    Нам нужно сбросить прибор SMBV100A. Для этого напишем следующую команду:

    >>> Driver('SMBV100A', 'set', 'reset')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "SMBV100A", "type": "set", "command": "reset"}'``

    Драйвер должен сбросить настройки прибора SMBV100A.

    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **3.**
    Нам нужно прочитать значение тестового окошка тестового драйвера. Для этого напишем следующую команду:

    >>> Driver('Test', 'get', 'test', 'bool')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "Test", "type": "get", "command": "test"}'``

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

    URLWrite = _UrlDriverWrite
    URLRead = _UrlDriverRead

    command_to_send = '{"name":"' + str(name) + '","type":"' + str(mode) + '","command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    drvdata = check_status("driver", mode, URLRead)
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

# Plugin - функция, осуществляющая работу с плагином
# name - имя плагина
# mode - тип команды ('get', 'set', 'init')
# command - команда, которую отправляем в плагин.
# valuetype (только для type = 'get') - тип данных, получаемый из плагина
def Plugin(name, mode, command, valuetype='void'):

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

    ``b'{"name": "NMEA0183", "type": "init", "command": ""}'``

    На экране должно появиться окно плагина.

    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **2.**
    Нам нужно сбросить протоколы плагина NMEA0183. Для этого напишем следующую команду:

    >>> Plugin("NMEA0183", "set", "ProtocolReset=True")

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "NMEA0183", "type": "set", "command": "ProtocolReset=True"}'``

    Плагин NMEA0183 должен сбросить протоколы.

    Функция должна вернуть следующее значение:

    ``None``
    
    Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **3.**
    Нам нужно прочитать время определения координат из плагина NMEA0183. Для этого напишем следующую команду:

    >>> Plugin('NMEA0183', 'get','CoordinatesValidTime', 'float')

    В случае успешного выполнения в терминале должна появиться следующая строка:
        
    ``b'{"name": "NMEA0183", "type": "get", "command": "CoordinatesValidTime"}'``

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

    URLWrite = _UrlPluginWrite
    URLRead = _UrlPluginRead

    command_to_send = '{"name":"' + str(name) + '","type":"' + str(mode) + '","command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    plgdata = check_status("plugin", mode, URLRead)
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

# Messenger - функция, осуществляющая появление на экране всплывающего сообщения с опциональным полем для ввода данных
# mode - тип команды ('get', 'set')
# head - заголовок сообщения
# body - содержание сообщения
# valuetype (только для type = 'get') - тип данных, получаемый из cообщения
# delaytime (если необходимо) - время задержки в секундах.
def Messenger(mode, head, body, valuetype='void', delaytime='void'):
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

    ``b'{"type": "set", "head": "Info", "body": "Please connect the device and launch NMEA0183 plugin."}'``
    
    На экране должно появиться окно с сообщением, в котором в заголовке будет написано 'Info', а в теле - 'Please connect the device and launch NMEA0183 plugin.'.
    
    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **2.**
    Нам нужно отобразить сообщение для пользователя, чтобы он ввёл некоторое число. Для этого напишем следующую команду:

    >>> Messenger('get', 'First number', 'Please, enter the first number', 'int')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"type": "get", "head": "First number", "body": "Please, enter the first number"}'``

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

    ``b'{"type": "set", "head": "Info", "body": "Please, wait for 15 minutes", "time": "900"}'``

    На экране должно появиться окно с сообщением, в котором в заголовке будет написано 'Info', а в теле - 'Please, wait for 15 minutes.'. 
    
    Также должен появиться таймер, отсчитывающий 15 минут.

    В случае какой-либо ошибки функция не выполняется, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None

    URLWrite = _UrlMessengerWrite
    URLRead = _UrlMessengerRead    
    
    if (delaytime == 'void'):
        command_to_send = '{"type":"'+str(mode)+'","head":"'+str(head)+'","body":"'+str(body)+'","value":"'+str(valuetype)+'"}'
    else:
        command_to_send = '{"type":"'+str(mode)+'","head":"'+str(head)+'","body":"'+str(body)+'","time":"'+str(delaytime)+'"}'

    send_request(URLWrite, command_to_send)

    msgdata = check_status("messenger", mode, URLRead)
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

# Report - функция, осуществляющая работу с данными в отчёте
# name - название для записываемых в отчёт данных и имя закладки в документе-шаблоне Word
# mode - тип команды (пока что только 'set') 
# kind - в каком виде данные записываются в отчёт(string - строка и table - таблица)
# data - записываемые в отчёт данные
# valuetype (только для mode = 'get') - тип данных, получаемый из отчёта
def Report(name, mode, kind, data, valuetype='void'):
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

    ``b'{"name": "rep1", "type": "set", "kind": "string", "data": "FgsFds"}'``

    В программе MOKO SE во вкладке 'Report' в таблице 'Report names' должен появиться элемент 'rep1'. По нажатию на этот элемент в таблице 'Reports' должна появиться строка *FgsFds*.
    
    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **2.**
    Нам нужно вывести 3 строки в таблицу отчёта. Для этого напишем следующую команду:

    >>> Report("rep2",'set', 'table', 'FgsFds, fgsfds, etc')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "rep2", "type": "set", "kind": "table", "data": "FgsFds, fgsfds, etc"}'``
    
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

    URLWrite = _UrlReportWrite
    URLRead = _UrlReportRead
    
    command_to_send = '{"name":"'+str(name)+'","type":"'+str(mode)+'", "kind":"'+str(kind)+'", "data":"'+str(data)+'"}'
    send_request(URLWrite, command_to_send)

    repdata = check_status("report", mode, URLRead)
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

# Utility - функция, осуществляющая работу с утилитой
# name - имя утилиты
# mode - тип команды ('get', 'set')
# command - команда, которую отправляем в утилиту.
# valuetype (только для type = 'get') - тип данных, получаемый из утилиты
def Utility(name, mode, command, valuetype='void'):

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

    URLWrite = _UrlUtilityWrite
    URLRead = _UrlUtilityRead

    command_to_send = '{"name" :"' + str(name) + '", "type":"' + str(mode) + '", "command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    utldata = check_status("utility", mode, URLRead)
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

# program - функция, осуществляющая управление программой MOKO SE (скриптами, проектами и т.д.)
# name - название типа, которым нужно управлять ('script', 'project', etc.)
# mode - тип команды (пока что только 'set') 
# command - команда, которую посылаем в MOKO SE
# valuetype (только для type = 'get') - получаемый тип данных
def Program(name, mode, command, valuetype='void'):
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

    b'{"name": "script", "type": "set", "command": "done"}'
    
    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    project_state()
    if is_mode_incorrect(mode, ["get", "set", "init", "close"]): return None
    if is_mode_and_valuetype_incorrect(mode, valuetype): return None

    URLWrite = _UrlProgramWrite
    URLRead = _UrlProgramRead

    command_to_send = '{"name":"' + str(name) + '","type":"' + str(mode) + '","command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    progdata = check_status("program", mode, URLRead)
    return parse_data(progdata, mode, valuetype)

def ProgramParam(name, param):
    URLRead = _UrlProgramRead + '/' + str(name) + '=' + str(param)

    response = requests.get(URLRead)	
    print(response.content)
    return

def EndScript(command='done'):
    """ 
    **Обязательная** функция, которая должна быть в конце каждого скрипта. Даёт знать серверу, что скрипт закончен.
    """
    res = Program('script','set',command)
    sys.exit()
    return res

def Script_CancelNumber(number):
    if (number.isdigit):
        res = Program('script','set','canceled = number ' + str(number))
    else:
        print('ERROR IN PYTHON LIBRARY! Wrong parameter for Cancel Number command! ' + str(number))
        res = Stage('ERROR IN PYTHON LIBRARY! Wrong parameter for Cancel Number command! ' + str(number),'error')
    return res

def Script_CancelName(name):
    res = Program('script','set','canceled = name ' + str(name))
    return res


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

# Telegram - функция, осуществляющая работу с Telegram
# role - имя драйвера ##############################
# mode - тип команды ('get', 'set')
# command - команда, которая передается в Telegram

def Telegram(role, mode, command, valuetype='void'):
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

    ``b'{"role": "alpha", "type": "set", "command": "Hello, I'm a bot!"}'``

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

    URLWrite = _UrlTelegramWrite
    URLRead = _UrlTelegramRead

    command_to_send = '{"role":"' + str(role) + '","type":"' + str(mode) + '","command":"' + str(command) + '"}'
    send_request(URLWrite, command_to_send)

    tgmdata = check_status("telegram", mode, URLRead)
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

def project_state():
    """
        project_state - предназначена для проверки старта/паузы/стопа
    """
    URLPSRead = _UrlProjectStateRead
    serverstate = requests.get(URLPSRead)
    JSONprojectstate = json.loads(serverstate.content)
    projectstate = JSONprojectstate.get('projectstate')
    while (projectstate.lower() != 'run'):
        sleep(0.05)
        serverstate = requests.get(URLPSRead)
        JSONprojectstate = json.loads(serverstate.content)
        projectstate = JSONprojectstate.get('projectstate')
        if (projectstate.lower() == 'stop'):
            sys.exit()
    return

def check_status(system, mode, URLRead):
    """
        check_status - предназначена для проверки статуса MOKO SE (ready или busy),
        а также для проверки status_code (если более 9 раз плохо приняты данные, то выдаем ошибку).

        :param str system: функция, которая вызывает (Driver, Program, ...)
        :param str mode: тип команды ('get', 'set', 'init', 'close', ...)
        :param str URLRead: URL для получения данных от сервера

        :return: Функция возвращает данные от сервера. Если badresponse > 9, то возвращается пустая строка (False)
    """
    data = ""
    timeout = 0
    badresponse = 0
    status = "none"
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
            status = y.get(f'{system}status')
            if (mode.lower() == 'get' or 'check'):
                data = y.get(f'{system}data')
            timeout += 1
        sleep(0.05)

    if is_bad_response(badresponse): return ""
    return data

def parse_data(data, mode, valuetype='void'):
    """
        parse_data - парсинг полученных данных в зависимости от переданного valuetype.

        :param str data: полученные данные
        :param str mode: тип команды ('get', 'set', 'init', 'close', ...)
        :param str valuetype: тип возвращаемых данных (только при mode = "get")

        :return: Функция возвращает данные того типа, который был указан в valuetype
    """
    if not (mode.lower() == "get" or "check"): return None

    splitter = ";"
    if is_semicolon_error(data, splitter, valuetype): return None

    if valuetype.lower() == 'boolean':
        data = data.split(splitter)[0]
        return True if data.lower() == "true" else False
    elif valuetype.lower() == 'float':
        data = data.split(splitter)[0]
        return float(data.replace(",", "."))
    elif valuetype.lower() == 'int':
        data = data.split(splitter)[0]
        data = data.split(".")[0]
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

def to_list(func, data, splitter=";"):
    """
        to_list - предназначена для разбиения входных данных с последующим занесением в список

        :param func: функция, которая применяется к данным (int(), float(), ...)
        :param str data: полученные данные
        :param str splitter: символ, по которому идет разбиение данных

        :return: Функция возвращает список, содержащий значения типа, соответствующих типу func() => (int, float, ...)
    """
    split_data = data.split(splitter)
    result = []
    for spl in split_data:
        if func is bool:
            result.append(True if spl.lower() == "true" else False)
        elif func is int:
            spl = spl.split(".")[0]
            result.append(func(spl.split(",")[0]))
        else:
            result.append(func(spl.replace(",", ".")))
    return result

def is_semicolon_error(data, splitter, valuetype):
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

def is_bad_response(badresponse):
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

def is_mode_and_valuetype_incorrect(mode, valuetype):
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

def is_mode_incorrect(mode, modes_list:list):
    """
        is_mode_correct - предназначена для проверки значения mode: корректное либо нет.

        :param str mode: тип команды ('get', 'set', 'init', 'close', ...)
        :param list modes_list: список mode, который корректен для данной функции (Driver, Program,...)

        :return: Функция печатает ошибку в консоль и в Stage программы MOKO SE, если в modes_list нет указанного mode.
                 Если ошибка - возвращает True, иначе - False
    """
    if mode.lower() not in modes_list:
        Stage("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode))
        return True
    return False

def send_request(URLWrite, command_to_send):
    """
        send_request - предназначена для отсылки команды/запроса на сервер

        :param str URLWrite: адрес сервера, для отправки команды/запроса
        :param command_to_send: команда/запрос, отправляемый на сервер в формате json

        :return: Функция возвращает None
    """
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(URLWrite, headers=headers, data=command_to_send.encode('utf-8'))
    print(response.content)
    return None