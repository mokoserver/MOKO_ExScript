import MOKO

MOKO.Report('Report', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
MOKO.Report('Report_clear', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
MOKO.Report('Report_delete', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')

MOKO.Report(f'Report', 'set', 'table', '1;2;3;4;5;6;7;8;9')
MOKO.Report(f'Report_clear', 'set', 'table', '1;2;3;4;5;6;7;8;9')
MOKO.Report(f'Report_delete', 'set', 'table', '1;2;3;4;5;6;7;8;9')

language = MOKO.Report('language', 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Save table
#hesh Save string
#hesh Save picture

if language == 'English':
    MOKO.Messenger('set', 'Report - save.jpg', 'This script will demonstrate the \'\'save\'\' command, '
                                           'which saves rows from Report to text files, '
                                           'tables to excel files, and pictures to png files. '
                                           'All this is stored in the \'\'data\'\' folder, which is created '
                                           '(if it does not exist) in the project folder.')
elif language == 'Русский':
    MOKO.Messenger('set', 'Report - save.jpg', 'В данном скрипте будет продемонстрирована команда \'\'save\'\', '
                                           'которая сохраняет строки из Report в текстовые файлы, '
                                           'таблицы в excel файлы, а картинки в png файлы. '
                                           'Всё это хранится в папке \'\'data\'\', которая создается (если не существует) '
                                           'в папке с проектом.')

screenshot = MOKO.Program('control', 'get', 'screenshot', 'string')
MOKO.Report('image_screenshot', 'set', 'picture', screenshot)
MOKO.Report('image_screenshot_clear', 'set', 'picture', screenshot)
MOKO.Report('image_screenshot_delete', 'set', 'picture', screenshot)

MOKO.Report("Report", 'save', 'string', 'csv')    # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Save table')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Report("language", 'save', 'string', 'txt')     # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Save string')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Report("image_screenshot", 'save', 'picture', 'png')  # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Save picture')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()