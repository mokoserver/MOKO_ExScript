import MOKO
import time

#Region Status (статус)
#hesh Delete table
#hesh Delete string
#hesh Delete picture

MOKO.Messenger('set', 'Report - delete#@delete', 'В текущем скрипте будет продемонстрирована команда \'\'delete\'\', '
                                                 'которая удаляет строки, таблицы и картинки в поле Report.')

MOKO.Report("Report_delete", 'delete', 'picture', '')   
MOKO.Program('tree', 'set', 'select = ' + 'Delete table')
MOKO.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

MOKO.Report("language_delete", 'delete', 'picture', '')    
MOKO.Program('tree', 'set', 'select = ' + 'Delete string')
MOKO.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

MOKO.Report("image_screenshot_delete", 'delete', 'picture', '')  
MOKO.Program('tree', 'set', 'select = ' + 'Delete picture')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()