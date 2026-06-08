import MOKO

#Region Status (статус)
#hash Report

MOKO.Program('control', 'set', 'save word report')
MOKO.Program('tree', 'set', 'select = ' + 'Report')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status (статус)


MOKO.EndScript()