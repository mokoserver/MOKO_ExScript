import MOKO as Moko
from MOSC import stars
import time

Moko.Stage(stars('*'))
Moko.Stage(stars('Новый SCRIPT'))
Moko.Stage(stars('*'))

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
Moko.Stage('*Telegram*. afafafaf', 'Telegram')
Moko.Stage('*Warning*. Информирует о предупреждении, произошедшем во время выполнения скрипта.', 'Warning')
time.sleep(6)
Moko.Report("exstage", 'set', 'string', 'Отсутствуют')
Moko.Report("exstage_1", 'set', 'string', 'Скрипт успешно завершён.')

Moko.Stage(stars('*'))
Moko.Stage(stars('Следующий SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()
