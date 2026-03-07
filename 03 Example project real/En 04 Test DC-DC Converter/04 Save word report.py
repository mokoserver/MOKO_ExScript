import MOKO
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Word report script', 'set', 'init', 'string')

MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Word report script *******************")
MOKO.Stage("*********************************************************")

#region Save word report$Word
MOSC.hashstatus("$Word")
MOKO.Program('tree', 'set', 'select = Save word report$Word')

MOKO.Stage("name: control >> mode: set >> command >> save word report", "Program")
MOKO.Program('control', 'set', 'save word report')

MOSC.hash_passed()
#endregion Save word report$Word

MOKO.EndScript()
