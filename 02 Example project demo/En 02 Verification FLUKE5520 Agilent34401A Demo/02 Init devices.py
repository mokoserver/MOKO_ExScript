import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Init devices script *******************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

#region Initialization devices$Init
MOSC.HeshStatus("$Init")
MOKO.Program('tree', 'set', 'select = Initialization devices$Init')

MOKO.Stage("*********************************************************")
MOKO.Messenger("set", 'Connect device#FLUKE5520_AGILENT34401.jpg',
               'Сonnect the device under test via the interface\n'
               'Reference equipment: FLUKE5520.\n'
               'Verified equipment: AGILENT34401.\n'
               'Verification procedure: example.', delaytime='10')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOSC.hesh_passed()
#endregion Initialization devices$Init

MOKO.EndScript()
