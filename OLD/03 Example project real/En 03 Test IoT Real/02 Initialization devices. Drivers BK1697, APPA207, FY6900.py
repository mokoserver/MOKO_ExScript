import MOKO
import MTLG
from SettingsAndMeasurement import Testing

MTLG.TelegramProgram('alpha', 'Initialization devices', 'set', 'init', 'string')

MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Init device  script *******************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")
MOKO.Stage("*********************************************************")

MOKO.Messenger("set", 'Test IoT#TestIoT.png',
               'For demo test IoT device. We will use 4 devices:\n'
               'FY6900; APPA207; BK PRECISION 1697; SDS1102',
               delaytime='5')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Report('DevicesUsed', 'info', 'table', 'Devices#300; Status#300;')

#region Initialization BK1697B$Init
MOKO.Program('tree', 'set', 'select = Initialization BK1697B$Init')

Testing.BK1697B.Initialization()

#endregion Initialization BK1697B$Init

#region Initialization FY6900$Init
MOKO.Program('tree', 'set', 'select = Initialization FY6900$Init')

Testing.FY6900.Initialization()

#endregion Initialization FY6900$Init

#region Initialization APPA207$Init
MOKO.Program('tree', 'set', 'select = Initialization APPA207$Init')

Testing.APPA207.Initialization()

#endregion Initialization APPA207$Init

Testing.check_simulation_mode()

Testing.BK1697B.SET_OUTPUT_OFF()

MOKO.EndScript()
