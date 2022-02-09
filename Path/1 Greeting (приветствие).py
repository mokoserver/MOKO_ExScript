import MOKO

#Region Status (статус)
#hesh Greeting

path_temp = 'D:\GitHub\MOKO\MOKO_ExScript\Path\data'

MOKO.Messenger('set', 'Language. Язык.jpg', '', f'path = {path_temp}')

pathFromWindow = MOKO.Messenger('get', 'Language. Язык.jpg', '', f'path = {path_temp}')

MOKO.Report('pathFromWindow', 'set', 'string', pathFromWindow)


MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()