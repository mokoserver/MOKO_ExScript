import MOKO
import time

#Region Status
#hesh Delete table
#hesh Delete string
#hesh Delete picture

MOKO.Messenger('set', 'Report - delete.jpg', 'The current script will demonstrate the \'\'delete\'\' command, '
                                             'which deletes rows, tables and pictures in the Report field.')

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
