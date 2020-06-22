import MokoRequestsLibrary as Moko
from MokoFormatedLibrary import stars
import time

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

Moko.Stage('Добро пожаловать в программу MOKO SE.')
Moko.Stage('Программа MOKO SE осуществляет управление программой MOKO NMEA и программами-драйверами')
Moko.Stage('Управление программой реализуется через выполнение скриптов написанных на Python.')
Moko.Stage('Данный скрипт реализуется через функцию Stage.')

Moko.Stage('Функция Stage может иметь определенный тип. Ниже представлен каждый из типов.')
Moko.Stage('*Info*. Выводит какую-либо информацию в Stage. Обозначен как тип по умолчанию', 'Info')
Moko.Stage('*Error*. Информирует об ошибке, произошедшей во время выполнения скрипта.', 'Error')
Moko.Stage('*Plugin*. Выводит информацию, связанную с плагином.', 'Plugin')
Moko.Stage('*Driver*. Выводит информацию, связанную с драйвером.', 'Driver')
Moko.Stage('*Report*. Информирует о записи данных в отчёт.', 'Report')
Moko.Stage('*Utility*. Сообщает об использовании утилиты.', 'Utility')
Moko.Stage('*Messenger*. Информирует о выводе окна Messenger.', 'Messenger')

Moko.Report("exstage", 'set', 'string', 'Скрипт успешно завершён.')

time.sleep(10)

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()