import MOKO
from Demo_Test_IoT import Testing
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

# MTLG.TelegramMessenger('set', 'Test IoT', 'For demo test IoT device. We will use 4 devices:\n'
#                                           'FY6900; APPA207; BK PRECISION 1697; SDS1102', 'string')
MOKO.Messenger("set", 'Test IoT#TestIoT.png',
               'For demo test IoT device. We will use 4 devices:\n'
               'FY6900; APPA207; BK PRECISION 1697; SDS1102',
               delaytime='5')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Report('DevicesUsed', 'info', 'table', 'Devices#300; Status#300;')

# MTLG.TelegramProgram('Init device BK1697B', 'init', '', 'string')
MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Init device BK1697B *******************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

Testing.BK1697B_INIT = MOKO.Driver('BK1697B', 'init', '', 'string')
MOKO.Report("DevicesUsed", "set", "table", f"BK1697B; {Testing.BK1697B_INIT}")
MOKO.Stage(" ")

# MTLG.TelegramProgram('Init device FY6900', 'init', '', 'string')
MOKO.Stage("*********************************************************")
MOKO.Stage("***************** Init device FY6900 ********************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

Testing.FY6900_INIT = MOKO.Driver('FY6900', 'init', '', 'string')
MOKO.Report("DevicesUsed", "set", "table", f"FY6900_INIT; {Testing.FY6900_INIT}")
MOKO.Stage(" ")

# MTLG.TelegramProgram('Init device APPA207', 'init', '', 'string')
MOKO.Stage("*********************************************************")
MOKO.Stage("**************** Init device APPA207 ********************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

Testing.APPA207_INIT = MOKO.Driver('APPA207', 'init', '', 'string')
MOKO.Report("DevicesUsed", "set", "table", f"APPA207; {Testing.APPA207_INIT}")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
# MTLG.TelegramMessenger('set', 'IoT devices connected successfully',
#                        'Devices:\n'
#                        'BK PRESICION 1697B connected successfully;\n'
#                        'FY6900 connected successfully;\n'
#                        'APPA207 connected successfully\n', 'string')
MOKO.Messenger("set", 'IoT devices connected successfully#TestIoT.png',
               'Devices:\n'
               'BK PRESICION 1697B connected successfully;\n'
               'FY6900 connected successfully;\n'
               'APPA207 connected successfully\n',
               delaytime='5')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

Testing.OutOFFCommand()

MOSC.hesh_passed()
#endregion Initialization devices$Init

MOKO.EndScript()
