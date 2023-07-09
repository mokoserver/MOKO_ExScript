import MOKO
import time

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Clear table
#hesh Clear string
#hesh Clear picture

if language == "English":
    MOKO.Messenger('set', 'Report - clear.jpg', 'This script will demonstrate the \'\'clear\'\' command, '
                                                'which clears the contents of rows, tables and pictures in the Report field.')
elif language == "Русский":
    MOKO.Messenger('set', 'Report - clear.jpg', 'В данном скрипте будет продемонстрирована команда \'\'clear\'\', '
                                                'которая очищает содержимое строк, таблиц и картинок в поле Report.')


MOKO.Report("Report_clear", 'clear', 'picture', 'png')  # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Clear table')
MOKO.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

MOKO.Report("language_clear", 'clear', 'picture', 'png')  # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Clear string')
MOKO.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

MOKO.Report("image_screenshot_clear", 'clear', 'picture', 'png') # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Clear picture')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()