import MOKO

#Region Status
#hash Save table
#hash Save string
#hash Save picture

MOKO.Messenger('set', 'Report - save.jpg', 'This script will demonstrate the \'\'save\'\' command, '
                                           'which saves rows from Report to text files, '
                                           'tables to excel files, and pictures to png files. '
                                           'All this is stored in the \'\'data\'\' folder, which is created '
                                           '(if it does not exist) in the project folder.')

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
