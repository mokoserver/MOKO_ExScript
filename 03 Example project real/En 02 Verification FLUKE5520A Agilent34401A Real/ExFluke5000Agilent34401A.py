import time

import MOKO
import MFRT
import MOSC


class ExFluke5000Agilent34401A:
    def __init__(self) -> None:
        self.FirstScriptStart, self.ContinueMeasurement = True, True
        self.RemeasurementNumber, self.TimeDelay, self.Count_meas = 0, 0, 0
        self.WireConnection = str()
        self.Remeasurement, self.Driver_start = False, False
        self.R4FirstResult = True
        self.LowerLimitResult, self.UpperLimitResult, self.Status = None, None, None
        self.AutomaticFluke5520A, self.AutomaticAgilent34401A, self.Simulation = False, False, False
        self.__init_connected_and_type_connected()
        
        
#######################################################################################################################
#######################################################  VDC  #########################################################
#######################################################################################################################

    def VDC_Measurement(self, range: (str | float | int), verified: (str | float | int), error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)
        
#######################################################################################################################
#####################################################  VDC MEAS  ######################################################
#######################################################################################################################

        MOKO.Stage(f'VDC Measure -> range = {range}, verified = {verified}, error = {error}')

        self.AgilentDMM_SET_RANGE(range=range)

        self.Fluke5520A_SET_VDC(verified=verified)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
####################################################  VDC REPORT  #####################################################
#######################################################################################################################

        MOKO.Report("VDC", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{MFRT.ConvertFloatToString(error)};"
                                           f"{self.Status}")

#######################################################################################################################
#######################################################  VAC  #########################################################
#######################################################################################################################

    def VAC_Measurement(self, range: (str | float | int), verified: (str | float | int), frequency: (str | float | int),
                        error: (str | float | int)) -> None:
        
        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
####################################################  VAC MEAS  #######################################################
#######################################################################################################################

        MOKO.Stage(f'VAC Measure -> range = {range}, verified = {verified}, frequency = {frequency}, error = {error}')

        self.AgilentDMM_SET_RANGE(range=range)

        self.Fluke5520A_SET_VAC(verified=verified, frequency=frequency)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
###################################################  VAC REPORT  ######################################################
#######################################################################################################################

        MOKO.Report("VAC", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{frequency};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#####################################################   R2  ###########################################################
#######################################################################################################################

    def R2_Measurement(self, range: (str | float | int), verified: (str | float | int),error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)
        
#######################################################################################################################
####################################################  R2 MEAS  ########################################################
#######################################################################################################################

        MOKO.Stage(f'R2 Measure -> range = {range}, verified = {verified}, error = {error}')

        self.AgilentDMM_SET_RANGE(range=range)

        self.Fluke5520A_SET_R(verified=verified)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
###################################################  R2 REPORT  #######################################################
#######################################################################################################################

        MOKO.Report("RES", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#####################################################   R4  ###########################################################
#######################################################################################################################

    def R4_Measurement(self, range: (str | float | int), verified: (str | float | int), error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
#####################################################  R4 MEAS  #######################################################
#######################################################################################################################

        MOKO.Stage(f'R4 Measure -> range = {range}, verified = {verified}, error = {error}')

        if self.R4FirstResult:
            
            self.Fluke5520A_SET_R(verified=0)
            time.sleep(3)
            self.AgilentDMM_SET_AUTOZERO_ONCE()
            
            self.R4FirstResult = False

        self.AgilentDMM_SET_RANGE(range=range)

        self.Fluke5520A_SET_R(verified=verified)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
##############################################  R4 REPORT  ############################################################
#######################################################################################################################

        MOKO.Report("RES", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#######################################################  IDC  #########################################################
#######################################################################################################################

    def IDC_Measurement(self, range: (str | float | int), verified: (str | float | int), error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
#####################################################  IDC MEAS  ######################################################
#######################################################################################################################

        MOKO.Stage(f'IDC Measure -> range = {range}, verified = {verified}, error = {error}')

        self.AgilentDMM_SET_RANGE(range=range)

        self.Fluke5520A_SET_IDC(verified=verified)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
####################################################  IDC REPORT  #####################################################
#######################################################################################################################

        MOKO.Report("IDC", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#######################################################  IAC  #########################################################
#######################################################################################################################

    def IAC_Measurement(self, range: (str | float | int), verified: (str | float | int), frequency: (str | float | int),
                        error: (str | float | int)) -> None:

        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

#######################################################################################################################
#####################################################  IAC MEAS  ######################################################
#######################################################################################################################

        MOKO.Stage(f'IAC Measure -> range = {range}, verified = {verified}, frequency = {frequency}, '
                   f'error = {error}')

        self.AgilentDMM_SET_RANGE(range=range)

        self.Fluke5520A_SET_IAC(verified=verified, frequency=frequency)

        f_result, accuracy = self.GetResultMeasurement(f_verified=f_verified, error=f_error, verified=verified)

#######################################################################################################################
###################################################  IAC REPORT  ######################################################
#######################################################################################################################

        MOKO.Report("IAC", "set", "table", f"{range};"
                                           f"{verified};"
                                           f"{frequency};"
                                           f"{MFRT.ConvertFloatToString(f_result, verified)};"
                                           f"{MFRT.ConvertFloatToString(accuracy, verified)};"
                                           f"{error};"
                                           f"{self.Status}")

#######################################################################################################################
#######################################################################################################################
########################################  Function get result measuare   ##############################################
#######################################################################################################################
#######################################################################################################################

    def GetResultMeasurement(self, f_verified: (float | int), error: (float | int), verified: str) -> (float, float):
        
        f_result, accuracy = 0, 0
        while self.ContinueMeasurement:

            if not self.Simulation:
                time.sleep(self.TimeDelay)
            else:
                time.sleep(0.1)
            
            result = self.Agilent34401A_Read_Result(verified=f_verified)
            
            f_result = MFRT.ConvertStringToFloat(result)
            
            if isinstance(f_result, str):
                continue
                
            accuracy = abs(f_verified - f_result)
            if accuracy > error and self.Remeasurement:
                if self.Count_meas >= self.RemeasurementNumber - 1:
                    choices = self.CallMessengerChoices(
                        verified=f_verified, error=error, result=f_result, reference_number=verified)
                    if choices:
                        continue
                else:
                    self.CallMessengerErrorPoint(
                        verified=f_verified, error=error, result=f_result, reference_number=verified)
                    continue

            if accuracy > error:
                self.Status = 'Failed'
                MOSC.hesh_failed()
            else:
                self.Status = 'OK'
                MOSC.hesh_passed()

            self.Count_meas = 0
            self.ContinueMeasurement = False
        return f_result, accuracy

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def MeasurementStartCommand(self, WireConnection: str) -> None:

        if not self.Driver_start:

            self.Agilent34401A_SET_FUNC(WireConnection=WireConnection)
            self.Agilent34401A_SET_RES_MIN()

            match WireConnection:
                case "VDC":
                    self.Agilent34401A_SET_NPLC_100()
                    self.Fluke5520A_SET_OUT_NORMAL()

                case "VAC":
                    self.Agilent34401A_SET_BAND_MIN()
                    self.Fluke5520A_SET_OUT_NORMAL()

                case "R2":
                    self.Agilent34401A_SET_NPLC_100()
                    self.Fluke5520A_SET_CONN_NO()

                case "R4":
                    self.Agilent34401A_SET_NPLC_100()
                    self.Fluke5520A_SET_OUT_NORMAL()
                    self.Fluke5520A_SET_CONN_4W()

                case "IDC":
                    self.Agilent34401A_SET_NPLC_100()
                    self.Fluke5520A_SET_OUT_AUX()

                case "IAC":
                    self.Agilent34401A_SET_BAND_MIN()
                    self.Fluke5520A_SET_OUT_AUX()

            self.Fluke5520A_SET_SwitchOFF_DIS()

            MOKO.Stage(" ")
            self.Driver_start = True

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def MeasurementStopCommand(self) -> None:

        self.Fluke5520A_SET_SwitchOFF_Enable()
        self.Fluke5520A_SET_STOP()

        self.Driver_start = False
        self.ContinueMeasurement = True

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################  Agilent34401A CHOICE CONNECTED  ##############################################
#######################################################################################################################
    def Agilent34401_Choice_Connected(self) -> str:
        if not self.Simulation:
            type_connected = MOKO.Messenger("get", "Choose a way to connect AGILENT34401A#@agilent34401a",
                                                         "Please select an Agilent34401A instrument setup type\n"
                                                               "Attention. By selecting simulation mode, "
                                                               "you run all measurements in simulation mode!!!",
                                                               "choice=Automatic;Manual;Simulation")
        else:
            type_connected = "Simulation"
            
        MOKO.Stage(" ")
        return type_connected
        
        
#######################################################################################################################
#########################################  Agilent34401A Init devices  ################################################
#######################################################################################################################

    def Agilent34401A_Init_Device(self) -> str:
        if self.Simulation:
            MOKO.Stage('Driver: AgilentDMM >> mode: init >> command: ', 'driver')
            return "connected"
        elif self.AutomaticAgilent34401A:
            return MOKO.Driver('AgilentDMM', 'init', '')
        else:
            MOKO.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nTurn on the device\nPress OK")
            
            return "connected"

#######################################################################################################################
###################################  Agilent34401A NOT SUCCESSFUL INIT devices  #######################################
#######################################################################################################################
    def Agilent34401_NOT_SUCCESSFUL_INIT(self) -> bool:
        return MOKO.Messenger("get", "AGILENT34401A initialization not successful#@agilent34401a",
                              "Failed to initialize AGILENT34401A. Do you want to continue measuring in "
                              "Manual mode?", "boolean")


#######################################################################################################################
##########################################  Agilent34401A SET TIMEOUT  ################################################
#######################################################################################################################

    def Agilent34401A_SET_TIMEOUT(self) -> None:
        if self.Simulation:
            MOKO.Stage('Driver: AgilentDMM >> mode: set >> command: Timeout = 10000', 'driver')
        elif self.AutomaticAgilent34401A:
            MOKO.Driver('AgilentDMM', 'set', 'Timeout = 10000')
        else:
            MOKO.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nSet Reset\nPress OK")

#######################################################################################################################
############################################  Agilent34401A SET RESET  ################################################
#######################################################################################################################

    def Agilent34401A_SET_RESET(self) -> None:
        if self.Simulation:
            MOKO.Stage('Driver: AgilentDMM >> mode: set >> command: Reset', 'driver')
        elif self.AutomaticAgilent34401A:
            MOKO.Driver('AgilentDMM', 'set', 'Reset')
        else:
            MOKO.Messenger("set", "Make settings Agilent34401A#@agilent34401a",
                           "Make settings:\nSet Timeout = 10000\nPress OK")

#######################################################################################################################
#############################################  Agilent34401A SET FUNC  ################################################
#######################################################################################################################

    def Agilent34401A_SET_FUNC(self, WireConnection: str) -> None:
            if self.Simulation:
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: func = {WireConnection} ', 'driver')
            elif self.AutomaticAgilent34401A:
                MOKO.Driver('AgilentDMM', 'set', f'func = {WireConnection}')
            else:
                MOKO.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                               f'Make settings:\nSet func = {WireConnection}\nPress OK')
            
            

#######################################################################################################################
#############################################  Agilent34401A SET NPLC  ################################################
#######################################################################################################################

    def Agilent34401A_SET_NPLC_100(self) -> None:
        if self.Simulation:
            MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: NPLC = 100 ', 'driver')
        elif self.AutomaticAgilent34401A:
            MOKO.Driver('AgilentDMM', 'set', 'NPLC = 100')
        else:
            MOKO.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           f'Make settings:\nSet NPLC = 100\nPress OK')

#######################################################################################################################
#############################################  Agilent34401A SET RES  #################################################
#######################################################################################################################

    def Agilent34401A_SET_RES_MIN(self) -> None:
        if self.Simulation:
            MOKO.Stage('Driver: AgilentDMM >> mode: set >> command: RES = MIN ', 'driver')
        elif self.AutomaticAgilent34401A:
            MOKO.Driver('AgilentDMM', 'set', 'RES = MIN')
        else:
            MOKO.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set Resolution = MIN;\nPress OK')

#######################################################################################################################
############################################  Agilent34401A SET BAND  #################################################
#######################################################################################################################

    def Agilent34401A_SET_BAND_MIN(self) -> None:

        if self.Simulation:
            MOKO.Stage('Driver: AgilentDMM >> mode: set >> command: BAND = 3 ', 'driver')
        elif self.AutomaticAgilent34401A:
            MOKO.Driver('AgilentDMM', 'set', 'BAND = 3')
        else:
            MOKO.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set the filter to 3 Hz;\nPress OK')

#######################################################################################################################
###########################################  Agilent34401A SET RANGE  #################################################
#######################################################################################################################
    def AgilentDMM_SET_RANGE(self, range: (str | float | int)) -> None:
        if self.Simulation:
            MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
        elif self.AutomaticAgilent34401A:
            MOKO.Driver('AgilentDMM', 'set', f'range = {range}')
        else:
            MOKO.Messenger("set", "Make settings on Agilent34401A#@agilent34401a",
                           f"Make settings:\nSet range = {range}\nPress OK")

#######################################################################################################################
##########################################  Agilent34401A SET AUTOZERO  ###############################################
#######################################################################################################################
    def AgilentDMM_SET_AUTOZERO_ONCE(self) -> None:
        if self.Simulation:
            MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: AUTOZERO = ONCE', 'driver')
        elif self.AutomaticAgilent34401A:
            MOKO.Driver('AgilentDMM', 'set', 'AUTOZERO = ONCE')
        else:
            MOKO.Messenger('set', 'Make settings on Agilent34401A#@agilent34401a',
                           'Set the resolution to 4th decimal places;\nClick OK')

#######################################################################################################################
##########################################  Agilent34401A READ RESULT  ################################################
#######################################################################################################################
    def Agilent34401A_Read_Result(self, verified: (int, float)) -> (str, int, float):
        if self.Simulation:
            MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
            result = verified
        elif self.AutomaticAgilent34401A:
            result = MOKO.Driver('AgilentDMM', 'get', 'read')
        else:
            result = MOKO.Messenger("get", "Input result#@notes",
                                    "Enter the measured result from Agilent34401A\nPress OK", "string")
        MOKO.Stage(" ")
        return result

#######################################################################################################################
#########################################  Fluke5520A CHOICE CONNECTED  ###############################################
#######################################################################################################################

    def Fluke5520A_Choice_Connected(self) -> str:
        if not self.Simulation:
            type_connected = MOKO.Messenger("get", "Choose a way to connect Fluke5520A#@fluke5520a",
                                            "Please select an Fluke5520A instrument setup type\n"
                                            "Attention. By selecting simulation mode, "
                                            "you run all measurements in simulation mode!!!",
                                            "choice=Automatic;Manual;Simulation")
        else:
            type_connected = "Simulation"

        MOKO.Stage(" ")
        return type_connected

#######################################################################################################################
############################################  Fluke5520A Init devices  ################################################
#######################################################################################################################

    def Fluke5520A_Init_Device(self) -> str:
        if self.Simulation:
            MOKO.Stage('Driver: Fluke5000 >> mode: init >> command: ', 'driver')
            return "connected"
        elif self.AutomaticFluke5520A:
            return MOKO.Driver('Fluke5000', 'init', '')
        else:
            MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           "Make settings:\nTurn on the device\nPress OK")

            return "connected"

#######################################################################################################################
######################################  Fluke5520A NOT SUCCESSFUL INIT devices  #######################################
#######################################################################################################################
    
    def Fluke5520A_NOT_SUCCESSFUL_INIT(self) -> bool:
        return MOKO.Messenger("get", "Fluke5520A initialization not successful#@fluke5520a",
                              "Failed to initialize Fluke5520A. Do you want to continue measuring in "
                              "Manual mode?", "boolean")

#######################################################################################################################
#############################################  Fluke5520A SET TIMEOUT  ################################################
#######################################################################################################################

    def Fluke5520A_SET_TIMEOUT(self) -> None:
        if self.Simulation:
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Timeout = 10000', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', 'Timeout = 10000')
        else:
            MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           "Make settings:\nSet Reset\nPress OK")

#######################################################################################################################
###############################################  Fluke5520A SET RESET  ################################################
#######################################################################################################################

    def Fluke5520A_SET_RESET(self) -> None:
        if self.Simulation:
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Reset', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', 'Reset')
        else:
            MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           "Make settings:\nSet Timeout = 10000\nPress OK")

#######################################################################################################################
############################################   Fluke5520 SET OUT = AUX   ##############################################
#######################################################################################################################

    def Fluke5520A_SET_OUT_AUX(self) -> None:
            if self.Simulation:
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = AUX', 'driver')
            elif self.AutomaticFluke5520A:
                MOKO.Driver('Fluke5000', 'set', 'OUT = AUX')
            else:
                MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                               'Make settings:\nSet OUT = AUX\nPress OK')

#######################################################################################################################
############################################   Fluke5520 SET OUT = NORMAL   ###########################################
#######################################################################################################################

    def Fluke5520A_SET_OUT_NORMAL(self) -> None:
            if self.Simulation:
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = NORMAL', 'driver')
            elif self.AutomaticFluke5520A:
                MOKO.Driver('Fluke5000', 'set', 'OUT = NORMAL')
            else:
                MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                               'Make settings:\nSet OUT = NORMAL\nPress OK')

#######################################################################################################################
############################################   Fluke5520 SET Conn = 4w  ###############################################
#######################################################################################################################

    def Fluke5520A_SET_CONN_4W(self) -> None:
            if self.Simulation:
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = 4w', 'driver')
            elif self.AutomaticFluke5520A:
                MOKO.Driver('Fluke5000', 'set', 'Conn = 4w')
            else:
                MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                            'Make settings:\nSet Conn = 4w\nPress OK')

#######################################################################################################################
############################################   Fluke5520 SET Conn = NO  ###############################################
#######################################################################################################################

    def Fluke5520A_SET_CONN_NO(self) -> None:
            if self.Simulation:
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = NO', 'driver')
            elif self.AutomaticFluke5520A:
                MOKO.Driver('Fluke5000', 'set', 'Conn = NO')
            else:
                MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                               'Make settings:\nSet Conn = NO\nPress OK')

#######################################################################################################################
###############################################   Fluke5520 SET VDC   #################################################
#######################################################################################################################
    def Fluke5520A_SET_VDC(self, verified: (str | float | int)) -> None:
        if self.Simulation:
            MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: VDC = {verified}', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', f'VDC = {verified}')
        else:
            MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet VDC = {verified}\nPress OK")

#######################################################################################################################
###############################################   Fluke5520 SET VAC   #################################################
#######################################################################################################################

    def Fluke5520A_SET_VAC(self, verified: (str | float | int), frequency: (str | float | int)) -> None:
        if self.Simulation:
            MOKO.Stage(f'DriverSet Fluke5000 >> mode: set >> command: VAC = {verified} {frequency}', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', f'VAC = {verified} {frequency}')
        else:
            MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet VAC = {verified} {frequency}\nPress OK")

#######################################################################################################################
###############################################   Fluke5520 SET R   ###################################################
#######################################################################################################################
    def Fluke5520A_SET_R(self, verified: (str | float | int)) -> None:
        if self.Simulation:
            MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: R = {verified}', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', f'R = {verified}')
        else:
            MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet R = {verified}\nPress OK")

#######################################################################################################################
###############################################   Fluke5520 SET IDC   #################################################
#######################################################################################################################
    def Fluke5520A_SET_IDC(self, verified: (str | float | int)) -> None:
        if self.Simulation:
            MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: IDC = {verified}', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', f'IDC = {verified}')
        else:
            MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet IDC = {verified}\nPress OK")

#######################################################################################################################
###############################################   Fluke5520 SET IAC   #################################################
#######################################################################################################################
    def Fluke5520A_SET_IAC(self, verified: (str | float | int), frequency: (str | float | int)) -> None:
        if self.Simulation:
            MOKO.Stage(f'DriverSet Fluke5000 >> mode: set >> command: IAC = {verified} {frequency}', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', f'IAC = {verified} {frequency}')
        else:
            MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                           f"Make settings:\nSet IAC = {verified} {frequency}\nPress OK")

#######################################################################################################################
#######################################   Fluke5520 SET SwitchOFF = Enable   ##########################################
#######################################################################################################################

    def Fluke5520A_SET_SwitchOFF_Enable(self) -> None:
        if self.Simulation:
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = ENABLE', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', 'SwitchOFF = ENABLE')
        else:
            MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet Stop\nPress OK')

#######################################################################################################################
##########################################   Fluke5520 SET SwitchOFF = DIS   ##########################################
#######################################################################################################################

    def Fluke5520A_SET_SwitchOFF_DIS(self) -> None:
        if self.Simulation:
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = DIS', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', 'SwitchOFF = DISABLE')
        else:
            MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet SwitchOFF = DISABLE\nPress OK')

#######################################################################################################################
##############################################   Fluke5520 SET STOP   #################################################
#######################################################################################################################

    def Fluke5520A_SET_STOP(self) -> None:
        if self.Simulation:
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Stop', 'driver')
        elif self.AutomaticFluke5520A:
            MOKO.Driver('Fluke5000', 'set', 'Stop')
        else:
            MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           'Make settings:\nSet Stop\nPress OK')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CheckWireConnection(self, WireConnection: str) -> None:
        
        if self.WireConnection != WireConnection:
            match WireConnection:
                case "VDC":
                    MOKO.Messenger('set',
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_V_R2.png',
                                   'Connect a multimeter to the calibrator to check VDC voltage.\n'
                                   'Calibrator output NORMAL')
                case "VAC":
                    MOKO.Messenger('set',
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_V_R2.png',
                                   'Connect a multimeter to the calibrator to check VAC voltage.\n'
                                   'Calibrator output NORMAL')
                case "R2":
                    MOKO.Messenger('set',
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_V_R2.png',
                                   'Connect a multimeter to the calibrator to check R2 resistance.\n'
                                   'Calibrator output NORMAL')
                case "R4":
                    MOKO.Messenger('set',
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_R4.png',
                                   'Connect a multimeter to the calibrator to check.\n'
                                   'RES resistance in 4-wire circuit.')
                case "IDC":
                    MOKO.Messenger("set",
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_I.png',
                                   'Connect a multimeter to the calibrator to test.\n'
                                   'DC current IDC up to 3 A.\n'
                                   'Calibrator output AUX up to 2 A.')
                case "IAC":
                    MOKO.Messenger("set",
                                   'Connecting wires#FLUKE5520A_AGILENT34401A_I.png',
                                   'Connect a multimeter to the calibrator to test.\n'
                                   'AC current IAC up to 3 A.\n'
                                   'Calibrator output AUX up to 2 A.')

            self.WireConnection = WireConnection
            MOKO.Stage(' ')

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CheckConnectDevices(self) -> None:
        if self.FirstScriptStart:
            MOKO.Stage('*****************************************************')
            MOKO.Stage('***************** Connect Devices *******************')
            MOKO.Stage('*****************************************************')

            self.InitializationAGILENT34401A(init=False)
            self.InitializationFluke5520A(init=False)

            self.FirstScriptStart = False

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def InitializationAGILENT34401A(self, init: bool = True):

        type_setting_agilent = self.Agilent34401_Choice_Connected()

        MOKO.Report("TYPE_SETTING_AGILENT34401A", "info", "string", "Device setting type")
        
        match type_setting_agilent:
            case 'Simulation':
                self.Simulation = True
                MOKO.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Simulation')
            case 'Automatic':
                self.AutomaticAgilent34401A = True
                MOKO.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Automatic')
            case "Manual":
                self.AutomaticAgilent34401A = False
                MOKO.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Manual')
            
        status_connected = self.Agilent34401A_Init_Device()
        
        if status_connected != 'connected':
            is_manual_connected = self.Agilent34401_NOT_SUCCESSFUL_INIT()
            if is_manual_connected:
                MOKO.Report("TYPE_SETTING_AGILENT34401A", "set", 'string', 'Manual')
                self.AutomaticAgilent34401A = False
            self.Agilent34401A_Init_Device()
        
        self.Agilent34401A_SET_TIMEOUT()
        self.Agilent34401A_SET_RESET()

#######################################################################################################################
        
        if init:
            if self.AutomaticAgilent34401A or self.Simulation:
                MOSC.hesh_passed()
            else:
                MOSC.hesh_failed()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def InitializationFluke5520A(self, init: bool = True) -> None:

        type_setting_fluke = self.Fluke5520A_Choice_Connected()

        MOKO.Report("TYPE_SETTING_FLUKE5520A", "info", "string", "Device setting type")

        match type_setting_fluke:
            case 'Simulation':
                self.Simulation = True
                MOKO.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', 'Simulation')
            case 'Automatic':
                self.AutomaticFluke5520A = True
                MOKO.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', 'Automatic')
            case "Manual":
                self.AutomaticFluke5520A = False
                MOKO.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', 'Manual')

        status_connected = self.Fluke5520A_Init_Device()

        if status_connected != 'connected':
            is_manual_connected = self.Fluke5520A_NOT_SUCCESSFUL_INIT()
            if is_manual_connected:
                MOKO.Report("TYPE_SETTING_FLUKE5520A", "set", 'string', 'Manual')
                self.AutomaticFluke5520A = False
            self.Fluke5520A_Init_Device()

        self.Fluke5520A_SET_TIMEOUT()
        self.Fluke5520A_SET_RESET()

#######################################################################################################################

        if init:
            if self.AutomaticFluke5520A or self.Simulation:
                MOSC.hesh_passed()
            else:
                MOSC.hesh_failed()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def SettingMeasurementLimits(self, verified: (float | int), error: (float | int)) -> None:
        self.LowerLimitResult = verified - error
        self.UpperLimitResult = verified + error

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CallMessengerChoices(self, verified: (float | int), error: (float | int), result: (float | int),
                             reference_number: str) -> str:

        self.SettingMeasurementLimits(verified=verified, error=error)

        limit_type = "lower" if self.LowerLimitResult > result else "upper"
        limit_value = self.LowerLimitResult - result if limit_type == "lower" else result - self.UpperLimitResult

        error_message = 'Do you want to repeat measuring this point?\n'
        error_message += f'Lower limit < Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.LowerLimitResult, reference_number)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, reference_number)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.UpperLimitResult, reference_number)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, reference_number)}'

        choices = MOKO.Messenger('get', 'The measurement result did not pass the specified limit#@repeat',
                                 error_message, 'boolean')

        self.Status = "Failed"
        self.Count_meas = 0
        return choices

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CallMessengerErrorPoint(self, verified: (float | int), error: (float | int), result: (float | int),
                                reference_number: str) -> None:

        self.SettingMeasurementLimits(verified=verified, error=error)

        limit_type = "lower" if self.LowerLimitResult > result else "upper"
        limit_value = self.LowerLimitResult - result if limit_type == "lower" else result - self.UpperLimitResult

        error_message = 'The measurement result did not pass the specified limit\n'
        error_message += 'The value is being remeasured\n'
        error_message += f'Lower limit <  Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.LowerLimitResult, reference_number)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, reference_number)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.UpperLimitResult, reference_number)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, reference_number)}'

        MOKO.Messenger('set', 'Measurement failed#@failed', error_message, delaytime='5')
        self.Count_meas += 1

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    @staticmethod
    def LoadTablesHeadInfo() -> None:
        MOKO.Report('VAC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Frequency#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        MOKO.Report('VDC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        MOKO.Report('RES', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        MOKO.Report('IAC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Frequency#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        MOKO.Report('IDC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        MOKO.Stage(" ")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def __init_connected_and_type_connected(self) -> None:
        type_setting_Fluke5520A = MOKO.Report("TYPE_SETTING_FLUKE5520A", "get", "string", "", 'string')
        type_setting_Agilent34401A = MOKO.Report("TYPE_SETTING_AGILENT34401A", "get", "string", "", 'string')

        if not type_setting_Agilent34401A or not type_setting_Fluke5520A:
            self.FirstScriptStart = True
            self.Simulation = False
            return
        else:
            self.FirstScriptStart = False

        if type_setting_Fluke5520A.lower() == 'simulation' or type_setting_Agilent34401A.lower() == 'simulation':
            self.Simulation = True
            return
        else:
            self.Simulation = False

        if type_setting_Fluke5520A.lower() == 'automatic':
            self.AutomaticFluke5520A = True
        else:
            self.AutomaticFluke5520A = False

        if type_setting_Agilent34401A.lower() == 'automatic':
            self.AutomaticAgilent34401A = True
        else:
            self.AutomaticAgilent34401A = False

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


Poverka = ExFluke5000Agilent34401A()
