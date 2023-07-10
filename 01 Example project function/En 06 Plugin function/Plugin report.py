import MOKO

MOKO.Program('control', 'set', 'save word report')

#Region Status

#hesh report
MOKO.Program('tree', 'set', 'select = ' + 'report')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()
