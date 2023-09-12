import MOSC
import MOKO


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class BK1697B:

    def __init__(self):
        self.IsAutomatic = False
        self.IsOutputON = False

#######################################################################################################################
##########################################  BK1697B CHOICE CONNECTED  #################################################
#######################################################################################################################

    def Choice_Connected(self) -> str:

        type_connected = MOKO.Messenger("get", "Choose a way to connect BK1697B#TestIoT.png",
                                                   "Please select an BK1697B instrument setup type\n"
                                                   "Attention. By selecting simulation mode, "
                                                   "you run all measurements in simulation mode!!!",
                                                   "choice=Automatic;Manual")

        MOKO.Stage(" ")
        return type_connected

#######################################################################################################################
###########################################  BK1697B Initialization  ##################################################
#######################################################################################################################

    def Initialization(self, init: bool = True) -> None:

        MOKO.Stage("*********************************************************")
        MOKO.Stage("***************** Init device BK1697B *******************")
        MOKO.Stage("*********************************************************")
        MOKO.Stage(" ")

        type_setting_bk = self.Choice_Connected()

        MOKO.Report("TYPE_SETTING_BK1697B", "info", "string", "Device setting type")
        MOKO.Stage(" ")

        match type_setting_bk:
            case 'Automatic':
                self.IsAutomatic = True
                MOKO.Report("TYPE_SETTING_BK1697B", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                MOKO.Report("TYPE_SETTING_BK1697B", "set", 'string', 'Manual')


########################################################################################################################

        if init:
            if self.IsAutomatic:
                MOKO.Report('DevicesUsed', 'set', 'table', 'BK1697B;Connected;')
                MOSC.hesh_passed()
            else:
                MOKO.Report('DevicesUsed', 'set', 'table', 'BK1697B;Disconnected;')
                MOSC.hesh_failed()

#######################################################################################################################
#############################################  BK1697B Init device  ###################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsAutomatic:
            MOKO.Stage('Driver: BK1697B >> mode: init >> command: ', 'driver')
            return "connected"
        else:
            MOKO.Messenger("set", "Make settings BK1697B#@attention",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"


#######################################################################################################################
###############################################  BK1697B SET VALUE  ###################################################
#######################################################################################################################

    def SET_VALUE(self, value: (float | int | str), Wireconnection: str) -> None:
        if self.IsAutomatic:
            MOKO.Stage(f"name -> BK1697B; mode -> set; command -> {Wireconnection} = {value}", 'driver')
        else:
            MOKO.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                       f"Set {Wireconnection} = {value}\n"
                                                                       "Press OK")

#######################################################################################################################
#############################################  BK1697B SET OUTPUT ON  #################################################
#######################################################################################################################

    def SET_OUTPUT_ON(self) -> None:
        if not self.IsOutputON:
            self.IsOutputON = True
            if self.IsAutomatic:
                MOKO.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = ON', 'set')
            else:
                MOKO.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                           "Set OUTPUT = ON\n"
                                                                           "Press OK")
            MOKO.Stage(" ")

#######################################################################################################################
############################################  BK1697B SET OUTPUT OFF  #################################################
#######################################################################################################################

    def SET_OUTPUT_OFF(self) -> None:
        self.IsOutputON = False
        if self.IsAutomatic:
            MOKO.Stage('name -> BK1697B; mode -> set; command -> OUTPUT = OFF', 'set')
        else:
            MOKO.Messenger("set", "Make settings BK1697B#TestIoT.png", "Make settings:\n"
                                                                       "Set OUTPUT = OFF\n"
                                                                       "Press OK")
