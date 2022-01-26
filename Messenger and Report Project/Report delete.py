import MOKO
import time

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Delete table
#hesh Delete string
#hesh Delete picture

if language == "English":
    MOKO.Messenger('set', 'Report - delete.jpg', 'The current script will demonstrate the \'\'delete\'\' command, '
                                             'which deletes rows, tables and pictures in the Report field.')

elif language == "Русский":
    MOKO.Messenger('set', 'Report - delete.jpg', 'В текущем скрипте будет продемонстрирована команда \'\'delete\'\', '
                                             'которая удаляет строки, таблицы и картинки в поле Report.')

MOKO.Report("Messenger_delete", 'delete', 'picture', '')   # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Delete table')
MOKO.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

MOKO.Report("language_delete", 'delete', 'picture', '')    # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Delete string')
MOKO.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

MOKO.Report("image_screenshot_delete", 'delete', 'picture', '')  # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Delete picture')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()