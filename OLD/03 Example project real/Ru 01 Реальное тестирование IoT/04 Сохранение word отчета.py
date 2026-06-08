import MOKO
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Сохранение Word отчета', 'set', 'init', 'string')

MOKO.Stage("*********************************************************")
MOKO.Stage("*************** Сохранение Word отчета ******************")
MOKO.Stage("*********************************************************")

#region Word отчет$Word
MOSC.hashStatus("$Word")
MOKO.Program('tree', 'set', 'select = Word отчет$Word')

MOKO.Stage("name: control >> mode: set >> command >> save word report", "Program")
MOKO.Program('control', 'set', 'save word report')

MOSC.hash_passed()
#endregion Word отчет$Word

MOKO.EndScript()
