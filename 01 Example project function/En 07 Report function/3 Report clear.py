import MOKO
import time

#Region Status
#hesh Clear table
#hesh Clear string
#hesh Clear picture

MOKO.Messenger('set', 'Report - clear.jpg', 'This script will demonstrate the \'\'clear\'\' command, '
                                                'which clears the contents of rows, tables and pictures in the Report field.')

MOKO.Report("Report_clear", 'clear', 'picture', 'png')  
MOKO.Program('tree', 'set', 'select = ' + 'Clear table')
MOKO.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

MOKO.Report("language_clear", 'clear', 'picture', 'png')  
MOKO.Program('tree', 'set', 'select = ' + 'Clear string')
MOKO.Program('tree', 'set', 'chosen = passed')
time.sleep(1)

MOKO.Report("image_screenshot_clear", 'clear', 'picture', 'png') 
MOKO.Program('tree', 'set', 'select = ' + 'Clear picture')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()
