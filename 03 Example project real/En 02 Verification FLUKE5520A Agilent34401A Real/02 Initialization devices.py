import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("************ Initialization devices script **************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Messenger("set", 'Connect device#FLUKE5520A_AGILENT34401.jpg',
               'Сonnect the device under test via the interface\n'
               'Reference equipment: FLUKE5520.\n'
               'Verified equipment: AGILENT34401.\n'
               'Verification procedure: example.', delaytime='10')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

#region Initialization AGILENT34401$Init
MOKO.Program('tree', 'set', 'select = Initialization AGILENT34401$Init')

TYPE_SETTING_AGILENT34401A = MOKO.Messenger("get", "Choose a way to connect AGILENT34401A#@agilent34401a",
                                                   "Please select an Agilent34401A instrument setup type",
                                                   "choice=Automatic; Manual")

MOKO.Report("TYPE_SETTING_AGILENT34401A", "info", "string", "Device setting type")
MOKO.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', TYPE_SETTING_AGILENT34401A)
MOKO.Stage(" ")

AGILENT34401A_INIT = str()
choices = None

if TYPE_SETTING_AGILENT34401A == 'Automatic':
    AGILENT34401A_INIT = MOKO.Driver('AgilentDMM', 'init', '')
    if AGILENT34401A_INIT != 'connected':
        choices = MOKO.Messenger("get", "AGILENT34401A initialization not successful#@agilent34401a", 
                                 "Failed to initialize AGILENT34401A. Do you want to continue measuring in "
                                 "Manual mode?", "boolean")
    if not choices or AGILENT34401A_INIT == 'connected':
        MOKO.Driver('AgilentDMM', 'set', 'Timeout = 10000')
        MOKO.Driver('AgilentDMM', 'set', 'Reset')
        MOSC.hesh_passed()
    else:
        MOSC.hesh_failed()
else:
    MOKO.Messenger("set", "Make settings Agilent34401A#@agilent34401a", "Make settings:\n"
                                                                        "Turn on the device\n"
                                                                        "Set Timeout = 10000\n"
                                                                        "Set Reset\n"
                                                                        "Press OK")
    MOSC.hesh_failed()

#endregion Initialization AGILENT34401$Init

#region Initialization FLUKE5520$Init
MOKO.Program('tree', 'set', 'select = Initialization AGILENT34401$Init')


TYPE_SETTING_FLUKE5520A = MOKO.Messenger("get", "Choose a way to connect FLUKE5520A#@fluke5520a",
                                                "Please select an FLUKE5520 instrument setup type",
                                                "choice=Automatic; Manual")

MOKO.Report("TYPE_SETTING_FLUKE5520A", "info", "string", "Device setting type")
MOKO.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', TYPE_SETTING_FLUKE5520A)
MOKO.Stage(" ")

Fluke5520_INIT = str()
choices = None

if TYPE_SETTING_FLUKE5520A == 'Automatic':
    FLUKE5520A_INIT = MOKO.Driver('Fluke5000', 'init', '')
    if FLUKE5520A_INIT != 'connected':
        choices = MOKO.Messenger("get", "Fluke5520A initialization not successful#@fluke5520a", 
                                 "Failed to initialize Fluke5520A. Do you want to continue measuring in "
                                 "Manual mode?", "boolean")
    if not choices or FLUKE5520A_INIT == 'connected':
        MOKO.Driver('Fluke5000', 'set', 'Timeout = 10000')
        MOKO.Driver('Fluke5000', 'set', 'Reset')
        MOSC.hesh_passed()
    else:
        MOSC.hesh_failed()
else:
    MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a", "Make settings:\n"
                                                                     "Turn on the device\n"
                                                                     "Set Timeout = 10000\n"
                                                                     "Set Reset\n"
                                                                     "Press OK")
    MOSC.hesh_failed()

#endregion Initialization FLUKE5520$Init

MOKO.EndScript()
