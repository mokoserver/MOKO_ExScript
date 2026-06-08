import MOKO

#Region Status
#hash Report

MOKO.Program('control', 'set', 'save word report')
MOKO.Program('tree', 'set', 'select = ' + 'Report')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status


MOKO.EndScript()