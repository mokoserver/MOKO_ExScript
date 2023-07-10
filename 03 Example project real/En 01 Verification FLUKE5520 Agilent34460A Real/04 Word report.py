import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Word report script *******************")
MOKO.Stage("*********************************************************")

#region Save word report$Word
MOSC.HeshStatus("$Word")
MOKO.Program('tree', 'set', 'select = Save word report$Word')

MOKO.Program('control', 'set', 'save word report')

MOSC.hesh_passed()
#endregion Save word report$Word

MOKO.EndScript()
