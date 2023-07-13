import MOKO
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Registration unit', 'set', 'init', 'string')
MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Init devices script *******************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")
MOKO.Stage("*********************************************************")

#region Initialization devices$Init
MOSC.HeshStatus("$Init")
MOKO.Program('tree', 'set', 'select = Initialization devices$Init')

MOKO.Messenger("set", 'Test IoT#TestIoT.png',
               'For demo test IoT device. We will use 4 devices:\n'
               'FY6900; APPA207; BK PRECISION 1697; SDS1102',
               delaytime='5')

MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Report('DevicesUsed', 'info', 'table', 'Devices#300; Status#300;')

MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Init device BK1697B *******************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("name -> BK1697B; mode -> set; command -> Init", 'driver')
MOKO.Report("DevicesUsed", "set", "table", f"BK1697B; connected")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Init device FY6900 ********************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("name -> FY6900; mode -> set; command -> Init", 'driver')
MOKO.Report("DevicesUsed", "set", "table", "FY6900; connected")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Stage("**************** Init device APPA207 ********************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("name -> APPA207; mode -> set; command -> Init", 'driver')
MOKO.Report("DevicesUsed", "set", "table", f"APPA207; connected")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")

MOKO.Messenger("set", 'IoT devices connected successfully#TestIoT.png',
               'Devices:\n'
               'BK PRESICION 1697B connected successfully;\n'
               'FY6900 connected successfully;\n'
               'APPA207 connected successfully\n',
               delaytime='5')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOSC.hesh_passed()
#endregion Initialization devices$Init

MOKO.EndScript()
