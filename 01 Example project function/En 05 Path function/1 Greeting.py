import MOKO

#Region Status
#hesh Greeting

path_temp = 'D:\GitHub\MOKO\MOKO_ExScript\Path\data'

MOKO.Messenger('set', 'Language.jpg', '', f'path = {path_temp}')

pathFromWindow = MOKO.Messenger('get', 'Language.jpg', '', f'path = {path_temp}')

MOKO.Report('pathFromWindow', 'set', 'string', pathFromWindow)


MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()
