'''
Библиотека MOKO.py
==================

Эта библиотека представляет собой Python-клиент для взаимодействия с программой MOKO SE.
Она позволяет управлять различными компонентами, плагинами и устройствами, подключенными к MOKO SE,
путем отправки HTTP-запросов на локальный сервер.

Ключевые возможности:
---------------------
- **Управление устройствами:** Взаимодействие с драйверами (`Driver`) и портами (`Port`).
- **Автоматизация GUI:** Управление элементами интерфейса внешних приложений (`Autoit`).
- **Взаимодействие с пользователем:** Отображение информационных окон и диалогов (`Messenger`).
- **Логирование и отчеты:** Отправка сообщений в лог (`Stage`) и управление отчетами (`Report`).
- **Управление системой:** Выполнение команд (`CMD`), работа с плагинами (`Plugin`) и утилитами (`Utility`).
- **Синхронизация:** Контроль за состоянием выполнения проекта (`check_project_state`).

Принцип работы:
---------------
Библиотека функционирует как API-обертка, отправляя POST-запросы в формате JSON на
HTTP-сервер, запущенный MOKO SE по адресу `http://localhost:55001`.

Зависимости:
-------------
- `requests`
- `json`

История версий:
---------------
- 26.02.2021: Библиотека переименована в MOKO.py.
- 23.06.2021 (v1.5): Изменен формат POST-запросов для драйверов.
- 24.01.2022: Внесены исправления для корректной работы команд start/pause/stop.
- 22.08.2022: Обновлена функция парсинга и проведена рефакторинг.
- 09.09.2022: Параметр 'type' заменен на 'mode' в JSON-запросах (обратная совместимость нарушена).
'''

import time
import requests
import json
import sys

requests = requests.Session()

# region ### URLs for MOKO SE API / URL-адреса для MOKO SE API ###
_BASE_URL = "http://localhost:55001/MOKOSE"

# --- Status ---
_UrlProjectStateRead: str = f"{_BASE_URL}/status/projectstate"

# --- Stage ---
_UrlStageWrite: str = f"{_BASE_URL}/stage/stagewrite"

# --- System Components ---
_UrlAutoitWrite: str = f"{_BASE_URL}/system/autoitwrite"
_UrlAutoitRead: str = f"{_BASE_URL}/system/autoitread"

_UrlDriverWrite: str = f"{_BASE_URL}/system/driverwrite"
_UrlDriverRead: str = f"{_BASE_URL}/system/driverread"

_UrlPluginWrite: str = f"{_BASE_URL}/system/pluginwrite"
_UrlPluginRead: str = f"{_BASE_URL}/system/pluginread"

_UrlMessengerWrite: str = f"{_BASE_URL}/system/messengerwrite"
_UrlMessengerRead: str = f"{_BASE_URL}/system/messengerread"

_UrlReportWrite: str = f"{_BASE_URL}/system/reportwrite"
_UrlReportRead: str = f"{_BASE_URL}/system/reportread"

_UrlProgramWrite: str = f"{_BASE_URL}/system/programwrite"
_UrlProgramRead: str = f"{_BASE_URL}/system/programread"

_UrlUtilityWrite: str = f"{_BASE_URL}/system/utilitywrite"
_UrlUtilityRead: str = f"{_BASE_URL}/system/utilityread"

_UrlTelegramWrite: str = f"{_BASE_URL}/system/telegramwrite"
_UrlTelegramRead: str = f"{_BASE_URL}/system/telegramread"

_UrlCmdWrite: str = f"{_BASE_URL}/system/cmdwrite"
_UrlCmdRead: str = f"{_BASE_URL}/system/cmdread"

_UrlPortWrite: str = f"{_BASE_URL}/system/portwrite"
_UrlPortRead: str = f"{_BASE_URL}/system/portread"
# endregion

# region ### MOKO SE API Functions / Функции MOKO SE API ###

# region --- CMD / Командная строка ---
def CMD(mode: str, command: str) -> ...:
    """
    Выполняет команду в командной строке (CMD) через MOKO SE.

    Args:
        mode (str): Режим выполнения команды. Возможные значения: ???.
        command (str): Команда для выполнения.

    Returns:
        str: Результат выполнения команды, возвращенный сервером. Формат: ???.
    """
    check_project_state()
    URLWrite: str = _UrlCmdWrite
    URLRead: str = _UrlCmdRead
    command_to_send: str = f'{{"mode":"{str(mode)}", "command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    cmddata: str = check_status("cmd", mode, URLRead)
    return cmddata
# endregion

# region --- Port / Порт ---
def Port(name: str, mode: str, command: str = '', valuetype: str = 'string') -> ...:
    """
    Управляет портами и устройствами, настроенными в MOKO SE.

    Позволяет инициализировать, настраивать, отправлять и получать данные с устройств,
    подключенных через различные интерфейсы (COM, LPT, и т.д.), используя их логическое имя.

    Args:
        name (str): Логическое имя порта/устройства, заданное в MOKO SE.
        mode (str): Режим работы. Основные значения: 'init', 'interface', 'write', 'read'.
        command (str, optional): Команда или данные для отправки в порт (используется в режиме 'write'). Defaults to ''.
        valuetype (str, optional): Ожидаемый тип данных при чтении (используется в режиме 'read'). Defaults to 'string'.

    Returns:
        str: Результат операции. Например:
             - Для 'init' и 'interface': 'ok' в случае успеха.
             - Для 'read': прочитанные данные.
             - В случае ошибки может возвращать 'error'.
    """
    check_project_state()
    URLWrite: str = _UrlPortWrite
    URLRead: str = _UrlPortRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    portdata: str = check_status("port", mode, URLRead)
    print(f"portdata = {portdata}")
    return portdata
# endregion

# region --- Autoit / Автоматизация GUI ---
def Autoit(title: str, classname: str, method: str, attributes: str = 'void') -> ...:
    """
    Взаимодействует с элементами GUI внешних приложений, используя технологию AutoIt.

    Позволяет автоматизировать действия в окнах, например, чтение текста из полей или нажатие кнопок.

    Args:
        title (str): Заголовок окна целевого приложения.
        classname (str): Имя класса элемента управления в окне (например, 'Edit1').
        method (str): Метод для выполнения над элементом (например, 'ControlGetText').
        attributes (str, optional): Дополнительные атрибуты для команды. Defaults to 'void'.

    Returns:
        str: Результат выполнения команды (например, полученный текст).
    """
    check_project_state()
    URLWrite: str = _UrlAutoitWrite
    URLRead: str = _UrlAutoitRead
    command_to_send: str = f'{{"title":"{str(title)}", "classname":"{str(classname)}","method":"{str(method)}","attributes":"{str(attributes)}"}}'
    send_request(URLWrite, command_to_send)
    autoitdata: str = check_status("autoit", method, URLRead)
    return autoitdata
# endregion

# region --- Stage / Логирование этапов ---
def Stage(stage_string: str, type: str = 'info') -> None:
    """
    Отправляет и отображает сообщение в окне "Stage" в MOKO SE.

    Используется для логирования и информирования пользователя во время выполнения скрипта.

    Args:
        stage_string (str): Текст сообщения для вывода.
        type (str, optional): Тип сообщения. Влияет на его отображение.
                              Возможные значения: 'Info', 'Error', 'Plugin', 'Driver', 'Report', 'Warning'.
                              Defaults to 'info'.
    """
    check_project_state()
    URLWrite: str = _UrlStageWrite
    command_to_send: str = f'{{"string" :"{str(stage_string)}", "type":"{str(type)}"}}'
    send_request(URLWrite, command_to_send)
# endregion

# region --- Driver / Драйвер ---
def Driver(name: str, mode: str, command: str = 'void', valuetype: str = 'string') -> ...:
    """
    Управляет драйверами устройств через MOKO SE.

    Args:
        name (str): Имя драйвера.
        mode (str): Режим работы с драйвером ('get', 'set', 'init', 'close').
        command (str, optional): Команда для драйвера. Defaults to 'void'.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'string'.

    Returns:
        Зависит от режима:
        - 'set', 'init', 'close': None
        - 'get': Данные, полученные от драйвера, преобразованные к типу `valuetype`.
    """
    check_project_state()
    URLWrite: str = _UrlDriverWrite
    URLRead: str = _UrlDriverRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    drvdata: str = check_status("driver", mode, URLRead)
    return parse_data(drvdata, mode, valuetype)
# endregion

# region --- Plugin / Плагин ---
def Plugin(name: str, mode: str, command: str = 'void', valuetype: str = 'void') -> ...:
    """
    Управляет плагинами в MOKO SE.

    Args:
        name (str): Имя плагина.
        mode (str): Режим работы с плагином ('get', 'set', 'init').
        command (str, optional): Команда для плагина. Defaults to 'void'.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set', 'init': None
        - 'get': Данные, полученные от плагина, преобразованные к типу `valuetype`.
    """
    check_project_state()
    URLWrite: str = _UrlPluginWrite
    URLRead: str = _UrlPluginRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    plgdata: str = check_status("plugin", mode, URLRead)
    return parse_data(plgdata, mode, valuetype)
# endregion

# region --- Messenger / Сообщения ---
def Messenger(mode: str, head: str = '', body: str = '', valuetype: str = 'void', delaytime: str = 'void') -> ...:
    """
    Отображает всплывающее окно (мессенджер) в MOKO SE для взаимодействия с пользователем.

    Args:
        mode (str): Режим окна ('get' для ввода данных, 'set' для отображения информации).
        head (str, optional): Заголовок окна. Defaults to ''.
        body (str, optional): Основной текст сообщения. Defaults to ''.
        valuetype (str, optional): Ожидаемый тип данных при вводе (только для mode='get'). Defaults to 'void'.
        delaytime (str, optional): Время (в секундах), на которое окно задержится на экране. Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set': None
        - 'get': Данные, введенные пользователем.
    """
    check_project_state()
    URLWrite: str = _UrlMessengerWrite
    URLRead: str = _UrlMessengerRead
    if (delaytime == 'void'):
        command_to_send: str = f'{{"mode":"{str(mode)}","head":"{str(head)}","body":"{str(body)}","value":"{str(valuetype)}"}}'
    else:
        command_to_send: str = f'{{"mode":"{str(mode)}","head":"{str(head)}","body":"{str(body)}","time":"{str(delaytime)}"}}'
    send_request(URLWrite, command_to_send)
    msgdata: str = check_status("messenger", mode, URLRead)
    return parse_data(msgdata, mode, valuetype)
# endregion

# region --- Report / Отчет ---
def Report(name: str, mode: str, kind: str = 'string', data: str = '', valuetype: str = 'void') -> ...:
    """
    Работает с данными в отчете MOKO SE.

    Args:
        name (str): Имя отчета или закладки в документе Word.
        mode (str): Режим работы ('get', 'set', ???).
        kind (str, optional): Тип записываемых данных ('string', 'table', 'picture'). Defaults to 'string'.
        data (str, optional): Данные для записи в отчет. Defaults to ''.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set': None
        - 'get': Данные, полученные из отчета.
    """
    check_project_state()
    URLWrite: str = _UrlReportWrite
    URLRead: str = _UrlReportRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}", "kind":"{str(kind)}", "data":"{str(data)}"}}'
    send_request(URLWrite, command_to_send)
    repdata: str = check_status("report", mode, URLRead)
    return parse_data(repdata, mode, valuetype)
# endregion

# region --- Utility / Утилита ---
def Utility(name: str, mode: str, command: str = 'void', valuetype: str = 'void') -> ...:
    """
    Управляет утилитами в MOKO SE.

    Args:
        name (str): Имя утилиты.
        mode (str): Режим работы ('get', 'set', ???).
        command (str, optional): Команда для утилиты. Defaults to 'void'.
        valuetype (str, optional): Ожидаемый тип данных при чтении (только для mode='get'). Defaults to 'void'.

    Returns:
        Зависит от режима:
        - 'set': None
        - 'get': Данные, полученные от утилиты.
    """
    check_project_state()
    URLWrite: str = _UrlUtilityWrite
    URLRead: str = _UrlUtilityRead
    command_to_send: str = f'{{"name" :"{str(name)}", "mode":"{str(mode)}", "command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    utldata: str = check_status("utility", mode, URLRead)
    return parse_data(utldata, mode, valuetype)
# endregion

# region --- Program / Программа ---
def Program(name: str, mode: str, command: str, valuetype: str = 'void') -> ...:
    """
    Управляет состоянием программы MOKO SE (скрипты, проекты и т.д.).

    Args:
        name (str): Тип управляемого объекта ('script', 'project', ???).
        mode (str): Режим работы (на данный момент только 'set').
        command (str): Выполняемая команда (например, 'done' для скрипта).
        valuetype (str, optional): Ожидаемый тип данных (для будущего режима 'get'). Defaults to 'void'.

    Returns:
        ???.
    """
    check_project_state()
    URLWrite: str = _UrlProgramWrite
    URLRead: str = _UrlProgramRead
    command_to_send: str = f'{{"name":"{str(name)}","mode":"{str(mode)}","command":"{str(command)}"}}'
    send_request(URLWrite, command_to_send)
    progdata: str = check_status("program", mode, URLRead)
    return parse_data(progdata, mode, valuetype)
# endregion

# region --- EndScript / Завершение скрипта ---
def EndScript(command: str = None) -> None:
    """
    Завершает выполнение текущего скрипта.

    Обязательная функция, которая должна вызываться в конце каждого скрипта,
    чтобы уведомить MOKO SE о его завершении.

    Args:
        command (str, optional): Команда, отправляемая серверу при завершении.
                                 Возможные значения:
                                 - 'done': Выполнено (желтый нейтральный цвет).
                                 - 'passed': Пройдено (зеленый цвет).
                                 - 'failed': Не пройдено (красный цвет).

                                 Также поддерживаются синонимы:
                                 - 'good' -> преобразуется в 'passed'
                                 - 'bad' -> преобразуется в 'failed'

                                 Если параметр не передан, автоматически получает
                                 статус из ScriptResult().
                                 Если передано неподдерживаемое значение,
                                 устанавливается статус 'failed'.
                                 Defaults to None.
    """
    if command is None:
        command = ScriptResult()

    # Нормализация значений
    command_lower = str(command).lower()

    # Преобразование синонимов
    if command_lower in {'good', 'passed'}:
        command = 'passed'
    elif command_lower in {'bad', 'failed'}:
        command = 'failed'
    elif command_lower == 'done':
        command = 'done'
    else:
        # Если ничего не подошло, пишем failed
        command = 'failed'

    Program('script', 'set', command)
    sys.exit()
# endregion

# region --- Tree & Hash / Дерево и Хэши ---

# -- ScriptResult --
def ScriptResult() -> str:
    """
    Получает результат выполнения текущего скрипта из дерева MOKO SE.

    Returns:
        str: Статус выполнения ('passed', 'failed', 'done').
    """
    return Program('tree', 'get', 'script status', 'string')

# -- ProjectResult --
def ProjectResult() -> str:
    """
    Получает результат выполнения всего проекта из дерева MOKO SE.

    Returns:
        str: Статус выполнения проекта ('passed', 'failed', 'done').
    """
    return Program('tree', 'get', 'ProjectStatus', 'string')

# -- SetHash --
def SetHash(command: str = 'done') -> None:
    """
    Устанавливает результат выполнения в дереве (Hash).

    Args:
        command (str, optional): Статус для установки.
                                 Возможные значения:
                                 - 'done': Выполнено (желтый нейтральный цвет).
                                 - 'passed': Пройдено (зеленый цвет).
                                 - 'failed': Не пройдено (красный цвет).
                                 Defaults to 'done'.
    """
    Program('tree', 'set', f'{command}')

# -- SelectCheckHash --
def SelectCheckHash(hash: str) -> bool:
    """
    Выбирает хэш в дереве и проверяет, является ли он пустым.

    Args:
        hash (str): Хэш для выбора и проверки.

    Returns:
        bool: True, если статус хэша 'empty', иначе False.
    """
    Program('tree', 'set', 'select = ' + hash)
    status = Program('tree', 'get', 'hash ' + hash, 'string')
    if status == 'empty':
        return True
    return False
# endregion

# region ### Internal Helper Functions / Внутренние вспомогательные функции ###

# region --- check_project_state / Проверка состояния проекта ---
def check_project_state() -> None:
    """
    Проверяет состояние проекта в MOKO SE и синхронизирует выполнение скрипта.

    - Если состояние 'run', продолжает выполнение.
    - Если состояние 'pause', приостанавливает скрипт до смены состояния.
    - Если состояние 'stop', немедленно завершает скрипт.
    """
    URLPSRead: str = _UrlProjectStateRead
    projectstate: str = ''
    while (projectstate.lower() != 'run'):
        serverstate = requests.get(URLPSRead)
        JSONprojectstate = json.loads(serverstate.content)
        projectstate: str = JSONprojectstate.get('projectstate')
        if (projectstate.lower() == 'stop'):
            sys.exit()
        if projectstate.lower() == 'pause':
            time.sleep(0.05)
# endregion

# region --- check_status / Проверка статуса ---
def check_status(system: str, mode: str, URLRead: str) -> str:
    """
    Ожидает готовности компонента MOKO SE и получает от него данные.

    Функция циклически опрашивает URLRead, пока статус компонента не станет 'ready'.
    Имеет 10 попыток, после чего возвращает пустую строку.

    Args:
        system (str): Имя системы/компонента (например, 'driver', 'plugin').
        mode (str): Режим, в котором была вызвана команда ('get', 'set', и т.д.).
        URLRead (str): URL для чтения статуса и данных.

    Returns:
        str: Строка с данными от компонента или пустая строка в случае ошибки.
    """
    data: str = ""
    badresponse: int = 0
    status: str = "none"
    while ((status.lower() != 'ready') and (badresponse < 10)):
        response = requests.get(URLRead)
        if (response.status_code != 200):
            Stage(f"ERROR IN PYTHON LIBRARY! BAD RESPONSE CODE! {str(response.status_code)}", 'error')
            print(f"ERROR IN PYTHON LIBRARY! BAD RESPONSE CODE! {str(response.status_code)}\n{str(10 - badresponse)} TRIES LEFT")
            badresponse += 1
        else:
            y = json.loads(response.content)
            status: str = y.get(f'{system}status')
            if (mode.lower() in ['get', 'check']):
                data: str = y.get(f'{system}data')
        if system in ['messenger', 'driver', 'plugin', 'utility']:
            time.sleep(0.05)
    if is_bad_response(badresponse): return ""
    return data
# endregion

# region --- parse_data / Разбор данных ---
def parse_data(data: str, mode: str, valuetype: str = 'void') -> ...:
    """
    Преобразует строковые данные от сервера в нужный тип Python.

    Поддерживает базовые типы (int, float, bool, str) и их массивы (arrayint, ...).

    Args:
        data (str): Входная строка данных от сервера.
        mode (str): Режим, в котором была вызвана команда. Парсинг выполняется только для 'get', 'check', 'init'.
        valuetype (str, optional): Целевой тип данных. Defaults to 'void'.

    Returns:
        Преобразованные данные или None, если парсинг не требуется или невозможен.
    """
    if mode.lower() not in ["get", "check", "init"]: return None
    splitter: str = ";"
    if is_semicolon_error(data, splitter, valuetype): return None
    data: str = check_data(data, splitter)
    if valuetype.lower() == 'arrayboolean':
        return to_list(bool, data, splitter)
    elif valuetype.lower() == 'arrayfloat':
        return to_list(float, data, splitter)
    elif valuetype.lower() == 'arrayint':
        return to_list(int, data, splitter)
    elif valuetype.lower() == 'arraystring':
        return to_list(str, data, splitter)
    elif "bool" in valuetype.lower():
        data: str = data.split(splitter)[0]
        return True if data.lower() == "true" else False
    elif valuetype.lower() == 'float':
        data: str = data.split(splitter)[0]
        return float(data.replace(",", "."))
    elif valuetype.lower() == 'int':
        data: str = data.split(splitter)[0]
        data: str = data.split(".")[0]
        return int(data.split(",")[0])
    else:  # Используется в качестве valuetype = 'string'
        return data.split(splitter)[0]
# endregion

# region --- check_data / Проверка данных ---
def check_data(data: str, splitter: str = ";") -> str:
    """
    Удаляет лишний символ-разделитель (';') в конце строки, если он есть.

    Args:
        data (str): Входная строка.
        splitter (str, optional): Символ-разделитель. Defaults to ";".

    Returns:
        str: Очищенная строка.
    """
    if data.endswith(splitter):
        data: str = data[:-1]
    return data
# endregion

# region --- to_list / Преобразовать в список ---
def to_list(func, data: str, splitter: str = ";") -> ...:
    """
    Разделяет строку на список и преобразует каждый элемент к заданному типу.

    Args:
        func: Функция преобразования типа (int, float, bool, str).
        data (str): Входная строка с данными, разделенными `splitter`.
        splitter (str, optional): Символ-разделитель. Defaults to ";".

    Returns:
        list: Список с преобразованными значениями.
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
# endregion

# region --- is_semicolon_error / Ошибка с точкой с запятой ---
def is_semicolon_error(data: str, splitter: str, valuetype: str) -> bool:
    """
    Проверяет наличие двойного разделителя (';;') в конце строки.

    Это считается ошибкой формата данных. При обнаружении выводит ошибку в Stage.

    Args:
        data (str): Входная строка.
        splitter (str): Символ-разделитель.
        valuetype (str): Тип значения, для которого производится проверка.

    Returns:
        bool: True, если ошибка найдена, иначе False.
    """
    if data.endswith(f"{splitter}{splitter}"):
        Stage(f'ERROR IN PYTHON LIBRARY!', 'error')
        Stage(f'INPUT DATA CONTAINS MORE THAN 1 \'{splitter}\' AT THE END!', 'error')
        Stage(f'DATA: {data}     =>     VALUETYPE: {valuetype.upper()}', 'error')
        print(f'ERROR IN PYTHON LIBRARY!')
        print(f'INPUT DATA CONTAINS MORE THAN 1 \'{splitter}\' AT THE END!')
        print(f'DATA: {data}     =>     VALUETYPE: {valuetype.upper()}')
        return True
    return False
# endregion

# region --- is_bad_response / Проверка плохого ответа ---
def is_bad_response(badresponse: int) -> bool:
    """
    Проверяет, не превышено ли количество неудачных ответов от сервера.

    Args:
        badresponse (int): Счетчик неудачных ответов.

    Returns:
        bool: True, если количество ошибок >= 10, иначе False.
    """
    if (badresponse >= 10):
        Stage("ERROR IN PYTHON LIBRARY! FUNCTION EXIT BECAUSE OF BAD RESPONSES", 'error')
        print("ERROR IN PYTHON LIBRARY! FUNCTION EXIT BECAUSE OF BAD RESPONSES")
        return True
    return False
# endregion

# region --- send_request / Отправка запроса ---
def send_request(URLWrite: str, request: str) -> None:
    """
    Отправляет POST-запрос на указанный URL с данными в формате JSON.

    Args:
        URLWrite (str): URL для отправки запроса.
        request (str): Тело запроса в виде строки JSON.
    """
    headers: dict = {'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(URLWrite, headers=headers, data=request.encode('utf-8'))
    print(response.content)
# endregion

# endregion