import MokoRequestsLibrary as Moko
from MokoFormatedLibrary import stars
import time
ex = __import__('01_01_Example_start')


Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

if ex.language == 'English (default)':
    # eng command
    Moko.Stage('Welcome to MOKO SE.')
    Moko.Stage('MOKO SE manages MOKO NMEA program and driver software.')
    Moko.Stage('Program control is implemented through the execution of scripts written in Python.')
    Moko.Stage('This script shows how the Stage function works.')

    Moko.Stage('Сообщения в Stage могут иметь определенный тип. Ниже представлен каждый из типов.')
    Moko.Stage('*Info*. Выводит какую-либо информацию в Stage. Обозначен как тип по умолчанию', 'Info')
    Moko.Stage('*Error*. Информирует об ошибке, произошедшей во время выполнения скрипта.', 'Error')
    Moko.Stage('*Plugin*. Выводит информацию, связанную с плагином.', 'Plugin')
    Moko.Stage('*Driver*. Выводит информацию, связанную с драйвером.', 'Driver')
    Moko.Stage('*Report*. Информирует о записи данных в отчёт.', 'Report')
    Moko.Stage('*Utility*. Сообщает об использовании утилиты.', 'Utility')
    Moko.Stage('*Messenger*. Информирует о выводе окна Messenger.', 'Messenger')

    time.sleep(10)

    Moko.Report("exstage", 'set', 'string', 'Отсутствуют')
    Moko.Report("exstage_1", 'set', 'string', 'Скрипт успешно завершён.')

elif ex.language == 'Русский':
    Moko.Stage('Добро пожаловать в программу MOKO SE.')
    Moko.Stage('Программа MOKO SE осуществляет управление программой MOKO NMEA и программами-драйверами')
    Moko.Stage('Управление программой реализуется через выполнение скриптов написанных на Python.')
    Moko.Stage('Данный скрипт демонстрирует работу функции Stage.')

    Moko.Stage('Сообщения в Stage могут иметь определенный тип. Ниже представлен каждый из типов.')
    Moko.Stage('*Info*. Выводит какую-либо информацию в Stage. Обозначен как тип по умолчанию', 'Info')
    Moko.Stage('*Error*. Информирует об ошибке, произошедшей во время выполнения скрипта.', 'Error')
    Moko.Stage('*Plugin*. Выводит информацию, связанную с плагином.', 'Plugin')
    Moko.Stage('*Driver*. Выводит информацию, связанную с драйвером.', 'Driver')
    Moko.Stage('*Report*. Информирует о записи данных в отчёт.', 'Report')
    Moko.Stage('*Utility*. Сообщает об использовании утилиты.', 'Utility')
    Moko.Stage('*Messenger*. Информирует о выводе окна Messenger.', 'Messenger')

    time.sleep(10)

    Moko.Report("exstage", 'set', 'string', 'Отсутствуют')
    Moko.Report("exstage_1", 'set', 'string', 'Скрипт успешно завершён.')

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()