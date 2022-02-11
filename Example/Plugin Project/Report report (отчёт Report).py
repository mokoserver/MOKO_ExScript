import MOKO

MOKO.Program('control', 'set', 'save word report')

#Region Status (статус)

#hesh report
MOKO.Program('tree', 'set', 'select = ' + 'report')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()