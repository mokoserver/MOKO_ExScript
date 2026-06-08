import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("*************** Save word report script *****************")
MOKO.Stage("*********************************************************")

#region Save word report$Word
MOSC.hashStatus("$Word")
MOKO.Program('tree', 'set', 'select = Save word report$Word')

MOKO.Program('control', 'set', 'save word report')

MOSC.hash_passed()
#endregion Save word report$Word

MOKO.EndScript()
