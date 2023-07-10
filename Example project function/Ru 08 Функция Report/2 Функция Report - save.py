import MOKO


#Region Status (статус)
#hesh Save table
#hesh Save string
#hesh Save picture

MOKO.Messenger('set', 'Report - save.jpg', 'В данном скрипте будет продемонстрирована команда \'\'save\'\', '
                                           'которая сохраняет строки из Report в текстовые файлы, '
                                           'таблицы в excel файлы, а картинки в png файлы. '
                                           'Всё это хранится в папке \'\'data\'\', которая создается (если не существует) '
                                           'в папке с проектом.')

screenshot = MOKO.Program('control', 'get', 'screenshot', 'string')
MOKO.Report('image_screenshot', 'set', 'picture', screenshot)
MOKO.Report('image_screenshot_clear', 'set', 'picture', screenshot)
MOKO.Report('image_screenshot_delete', 'set', 'picture', screenshot)

MOKO.Report("Report", 'save', 'string', 'csv')    
MOKO.Program('tree', 'set', 'select = ' + 'Save table')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Report("language", 'save', 'string', 'txt')     
MOKO.Program('tree', 'set', 'select = ' + 'Save string')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Report("image_screenshot", 'save', 'picture', 'png')  
MOKO.Program('tree', 'set', 'select = ' + 'Save picture')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()
