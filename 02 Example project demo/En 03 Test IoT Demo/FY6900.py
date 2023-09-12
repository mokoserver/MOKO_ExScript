import MOSC
import MOKO


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

class FY6900:

    def __init__(self):
        self.IsAutomatic = False

#######################################################################################################################
##########################################  FY6900 CHOICE CONNECTED  ##################################################
#######################################################################################################################

    def Choice_Connected(self) -> str:

        type_connected = MOKO.Messenger("get", "Choose a way to connect FY6900#TestIoT.png",
                                            "Please select an FY6900 instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual;Simulation")

        MOKO.Stage(" ")

        return type_connected

#######################################################################################################################
###########################################  FY6900 Initialization  ###################################################
#######################################################################################################################

    def Initialization(self, init: bool = True) -> None:

        MOKO.Stage("*********************************************************")
        MOKO.Stage("***************** Init device BK1697B *******************")
        MOKO.Stage("*********************************************************")
        MOKO.Stage(" ")

        type_setting_fy = self.Choice_Connected()

        MOKO.Report("TYPE_SETTING_FY6900", "info", "string", "Device setting type")
        MOKO.Stage(" ")

        match type_setting_fy:
            case 'Automatic':
                self.IsAutomatic = True
                MOKO.Report("TYPE_SETTING_FY6900", "set", 'string', 'Automatic')
            case "Manual":
                self.IsAutomatic = False
                MOKO.Report("TYPE_SETTING_FY6900", "set", 'string', 'Manual')

########################################################################################################################

        if init:
            if self.IsAutomatic:
                MOKO.Report('DevicesUsed', 'set', 'table', 'FY6900;Connected;')
                MOSC.hesh_passed()
            else:
                MOKO.Report('DevicesUsed', 'set', 'table', 'FY6900;Disconnected;')
                MOSC.hesh_failed()

#######################################################################################################################
############################################  FY6900 Init device  #####################################################
#######################################################################################################################

    def INIT_DEVICE(self) -> str:
        if self.IsAutomatic:
            MOKO.Stage('Driver: FY6900 >> mode: init >> command: ', 'driver')
            return "connected"
        else:
            MOKO.Messenger("set", "Make settings FY6900#@attention",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"

#######################################################################################################################
###############################################  FY6900 SET WAVE  #####################################################
#######################################################################################################################

    def SET_WAVE(self, wave):
        if self.IsAutomatic:
            MOKO.Stage(f"name -> FY6900; mode -> set; command -> WAVE = {wave}", 'driver')
        else:
            MOKO.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set WAVE = {wave}\n"
                                                                      "Press OK")

#######################################################################################################################
#############################################  FY6900 SET AMPLITUDE  ##################################################
#######################################################################################################################

    def SET_AMPLITUDE(self, amplitude):
        if self.IsAutomatic:
            MOKO.Stage(f"name -> FY6900; mode -> set; command -> amplitude = {amplitude}", 'driver')
        else:
            MOKO.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set amplitude = {amplitude}\n"
                                                                      "Press OK")

#######################################################################################################################
#############################################  FY6900 SET FREQUENCY  ##################################################
#######################################################################################################################

    def SET_FREQUENCY(self, frequency):
        if self.IsAutomatic:
            MOKO.Stage(f"name -> FY6900; mode -> set; command -> frequency = {frequency}", 'driver')
        else:
            MOKO.Messenger("set", "Make settings FY6900#TestIoT.png", "Make settings:\n"
                                                                      f"Set frequency = {frequency}\n"
                                                                      "Press OK")
