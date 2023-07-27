import MOKO
import MTLG
from Demo_Test_IoT_4_Wave import Testing

MTLG.TelegramProgram('alpha', 'Инициализация устройств', 'set', '', 'string')

MOKO.Stage("*********************************************************")
MOKO.Stage("*************** Инициализация устройств *****************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")
MOKO.Stage("*********************************************************")

MOKO.Messenger("set", 'Тестирование IoT#TestIoT.png',
               'Tестированиe устройств IoT. Мы будем использовать 4 устройства\n'
               'FY6900; APPA207; BK PRECISION 1697; SDS1102',
               delaytime='5')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Report('DevicesUsed', 'info', 'table', 'Devices#300; Status#300;')

#region Инициализация BK1697B$Init
MOKO.Program('tree', 'set', 'select = Инициализация BK1697B$Init')

Testing.InitializationBK1697B()

#endregion Инициализация BK1697B$Init

#region Инициализация FY6900$Init
MOKO.Program('tree', 'set', 'select = Инициализация FY6900$Init')

Testing.InitializationFY6900()

#endregion Инициализация FY6900$Init

#region Инициализация APPA207$Init
MOKO.Program('tree', 'set', 'select = Инициализация APPA207$Init')

Testing.InitializationAPPA207()

#endregion Инициализация APPA207$Init

MOKO.EndScript()
