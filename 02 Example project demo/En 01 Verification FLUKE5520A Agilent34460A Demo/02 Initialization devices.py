import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("************ Initialization devices script **************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Messenger("set", 'Connect device#FLUKE5520A_AGILENT34460A.jpg',
               'Сonnect the device under test via the interface\n'
               'Reference equipment: FLUKE5520.\n'
               'Verified equipment: AGILENT34460.\n'
               'Verification procedure: example.', delaytime='10')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

#region Initialization AGILENT34460$Init
MOKO.Program('tree', 'set', 'select = Initialization AGILENT34460$Init')

TYPE_SETTING_AGILENT34460A = MOKO.Messenger("get", "Choose a way to connect AGILENT34460A#@agilent34460a",
                                                   "Please select an Agilent34460A instrument setup type",
                                                   "choice=Automatic;Manual")

MOKO.Report("TYPE_SETTING_AGILENT34460A", "info", "string", "Device setting type")
MOKO.Report("TYPE_SETTING_AGILENT34460A", "set", 'string', TYPE_SETTING_AGILENT34460A)
MOKO.Stage(" ")

AGILENT34460A_INIT = str()
choices, simulation = None, False

###############################################   AGILENT34460A Init   ################################################
###########################################   AGILENT34460A SET Timeout  ##############################################
if TYPE_SETTING_AGILENT34460A == 'Automatic':
    MOKO.Stage('Driver: AgilentDMM >> mode: init >> command: ', 'driver')
    AGILENT34460A_INIT = 'connected'
    if AGILENT34460A_INIT != 'connected':
        choices = MOKO.Messenger("get", "AGILENT34460A initialization not successful#@agilent34460a",
                                 "Failed to initialize AGILENT34460A. Do you want to continue measuring in "
                                 "Manual mode?", "boolean")
    if not choices or AGILENT34460A_INIT == 'connected':
        MOKO.Stage('Driver: AgilentDMM >> mode: set >> command: Timeout = 10000', 'driver')
        MOSC.hesh_passed()
    else:
        TYPE_SETTING_AGILENT34460A = 'Manual'
        MOKO.Messenger("set", "Make settings Agilent34460A#@agilent34460a", "Make settings:\n"
                                                                        "Turn on the device\n"
                                                                        "Set Timeout = 10000\n"
                                                                        "Press OK")
    MOSC.hesh_failed()

else:
    MOKO.Messenger("set", "Make settings Agilent34460A#@agilent34460a", "Make settings:\n"
                                                                        "Turn on the device\n"
                                                                        "Set Timeout = 10000\n"
                                                                        "Press OK")
    MOSC.hesh_failed()

#######################################################################################################################

#endregion Initialization AGILENT34460$Init

#region Initialization FLUKE5520A$Init
MOKO.Program('tree', 'set', 'select = Initialization FLUKE5520A$Init')

TYPE_SETTING_FLUKE5520A = MOKO.Messenger("get", "Choose a way to connect FLUKE5520A#@fluke5520a",
                                                "Please select an FLUKE5520 instrument setup type",
                                                "choice=Automatic;Manual")


MOKO.Report("TYPE_SETTING_FLUKE5520A", "info", "string", "Device setting type")
MOKO.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', TYPE_SETTING_FLUKE5520A)
MOKO.Stage(" ")

Fluke5520_INIT = str()
choices = None

###################################################   Fluke5520 Init   ################################################
###############################################   Fluke5520 SET Timeout  ##############################################
################################################   Fluke5520 SET Reset  ###############################################
if TYPE_SETTING_FLUKE5520A == 'Automatic':
    MOKO.Stage('Driver: Fluke5000 >> mode: init >> command: ', 'driver')
    FLUKE5520A_INIT = 'connected'
    if FLUKE5520A_INIT != 'connected':
        choices = MOKO.Messenger("get", "Fluke5520A initialization not successful#@fluke5520a",
                                 "Failed to initialize Fluke5520A. Do you want to continue measuring in "
                                 "Manual mode?", "boolean")
    if not choices or FLUKE5520A_INIT == 'connected':
        MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Timeout = 10000', 'driver')
        MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Reset', 'driver')
        MOSC.hesh_passed()
    else:
        TYPE_SETTING_FLUKE5520A = 'Manual'
        MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a", "Make settings:\n"
                                                                         "Turn on the device\n"
                                                                         "Set Timeout = 10000\n"
                                                                         "Set Reset\n"
                                                                         "Press OK")
        MOSC.hesh_failed()
else:
    MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a", "Make settings:\n"
                                                                     "Turn on the device\n"
                                                                     "Set Timeout = 10000\n"
                                                                     "Set Reset\n"
                                                                     "Press OK")
    MOSC.hesh_failed()

#######################################################################################################################

#endregion Initialization FLUKE5520A$Init

MOKO.EndScript()
