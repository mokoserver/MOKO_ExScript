import MOSC
import MOKO


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class APPA207:

    def __init__(self):
        self.IsAutomatic = False
        self.IsSimulation = False

#######################################################################################################################
##########################################  APPA207 CHOICE CONNECTED  #################################################
#######################################################################################################################

    def Choice_Connected(self) -> str:

        type_connected = MOKO.Messenger("get", "Choose a way to connect APPA207#TestIoT.png",
                                            "Please select an APPA207 instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual")

        MOKO.Stage(" ")
        return type_connected

#######################################################################################################################
###########################################  APPA207 Initialization  ##################################################
#######################################################################################################################

    def Initialization(self, init: bool = True) -> None:

        MOKO.Stage("*********************************************************")
        MOKO.Stage("**************** Init device APPA207 ********************")
        MOKO.Stage("*********************************************************")
        MOKO.Stage(" ")

        type_setting_appa = self.Choice_Connected()

        MOKO.Report("TYPE_SETTING_APPA207", "info", "string", "Device setting type")
        MOKO.Stage(" ")

        match type_setting_appa:
            case 'Automatic':
                self.IsAutomatic = True
                MOKO.Report("TYPE_SETTING_APPA207", "set", 'string', 'Automatic')

            case "Manual":
                self.IsAutomatic = False
                MOKO.Report("TYPE_SETTING_APPA207", "set", 'string', 'Manual')

        self.INIT_DEVICE()


########################################################################################################################

        if init:
            if self.IsAutomatic:
                MOKO.Report('DevicesUsed', 'set', 'table', 'APPA207;Connected;')
                MOSC.hash_passed()
            else:
                MOKO.Report('DevicesUsed', 'set', 'table', 'APPA207;Disconnected;')
                MOSC.hash_failed()

#######################################################################################################################
#############################################  APPA207 Init device  ###################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsAutomatic:
            MOKO.Stage('Driver: APPA207 >> mode: init >> command: ', 'driver')
            return "connected"
        else:
            MOKO.Messenger("set", "Make settings APPA207#@attention",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"


#######################################################################################################################
###########################################  APPA207 READ RESULT  #####################################################
#######################################################################################################################

    def READ_RESULT(self, value: (float | int)) -> str:
        if self.IsAutomatic:
            MOKO.Stage(f"name -> APPA207; mode -> get; command -> read", 'driver')
            result = str(value)
        else:
            result = MOKO.Messenger("get", "Input result#@notes",
                                    "Enter the measured result from APPA207\nPress OK", "string")

        MOKO.Stage(" ")
        return result
