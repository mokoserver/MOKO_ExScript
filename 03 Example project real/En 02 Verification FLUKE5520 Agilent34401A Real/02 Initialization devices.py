import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("************ Initialization devices script **************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Messenger("set", 'Connect device#FLUKE5520_AGILENT34401.jpg',
               'Сonnect the device under test via the interface\n'
               'Reference equipment: FLUKE5520.\n'
               'Verified equipment: AGILENT34401.\n'
               'Verification procedure: example.', delaytime='10')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

#region Initialization AGILENT34401$Init
MOKO.Program('tree', 'set', 'select = Initialization AGILENT34401$Init')

TYPE_SETTING_AGILENT34401A = MOKO.Messenger("get", "Choose a way to connect AGILENT34401#@agilent34401a",
                                                   "Please select an Agilent34401A instrument setup type",
                                                   "choice=Automatic; Manual")

MOKO.Report("TYPE_SETTING_AGILENT34401A", "info", "string", "Device setting type")
MOKO.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', TYPE_SETTING_AGILENT34401A)
MOKO.Stage(" ")

AGILENT34401A_INIT = str()

if TYPE_SETTING_AGILENT34401A == 'Automatic':

    AGILENT34401A_INIT = MOKO.Driver('AgilentDMM', 'init', '')

    MOKO.Driver('AgilentDMM', 'set', 'Timeout = 10000')
    MOKO.Driver('AgilentDMM', 'set', 'Reset')

    MOSC.hesh_passed()


else:
    MOKO.Messenger("set", "Make settings Agilent34401A#@attention", "Make settings:\n"
                                                                     "Turn on the device\n"
                                                                     "Set Timeout = 10000\n"
                                                                     "Set Reset\n"
                                                                     "Press OK")
    MOSC.hesh_failed()

MOKO.Report("STATUS_CONNECTED_AGILENT34401A", "set", "string", "connected")

#endregion Initialization AGILENT34401$Init

#region Initialization FLUKE5520$Init
MOKO.Program('tree', 'set', 'select = Initialization AGILENT34401$Init')


TYPE_SETTING_FLUKE5000 = MOKO.Messenger("get", "Choose a way to connect FLUKE5520#@fluke5520a",
                                               "Please select an FLUKE5520 instrument setup type",
                                               "choice=Automatic; Manual")

MOKO.Report("TYPE_SETTING_FLUKE5520", "info", "string", "Device setting type")
MOKO.Report("TYPE_SETTING_FLUKE5520", "set", 'string', TYPE_SETTING_FLUKE5000)
MOKO.Stage(" ")

Fluke5520_INIT = str()

if TYPE_SETTING_FLUKE5000 == 'Automatic':

    MOKO.Driver('Fluke5000', 'init', '')

    MOKO.Driver('Fluke5000', 'set', 'Timeout = 10000')
    MOKO.Driver('Fluke5000', 'set', 'Reset')

    MOSC.hesh_passed()

else:
    MOKO.Messenger("set", "Make settings on Fluke5520#@attention", "Make settings:\n"
                                                                   "Turn on the device\n"
                                                                   "Set Timeout = 10000\n"
                                                                   "Set Reset\n"
                                                                   "Press OK")
    MOSC.hesh_failed()

MOKO.Report("STATUS_CONNECTED_FLUKE5520", "set", "string", "connected")

#endregion Initialization FLUKE5520$Init

MOKO.EndScript()
