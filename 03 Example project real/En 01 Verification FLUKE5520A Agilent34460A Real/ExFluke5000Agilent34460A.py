import time

import MOKO
import MFRT


class ExFluke5000Agilent34460A:
    def __init__(self) -> None:
        self.FirstScriptStart, self.ContinueMeasurement = True, True
        self.RemeasurementNumber, self.TimeDelay, self.Count_meas = 0, 0, 0
        self.WireConnection = str()
        self.Remeasurement, self.Driver_start = False, False
        self.LowerLimitResult, self.UpperLimitResult, self.Status = None, None, None
        self.AutomaticFluke5520, self.AutomaticAgilent34460A, self.Simulation = False, False, False
        self.AGILENT34460A_INIT, self.FLUKE5520A_INIT = str(), str()
        self.__init_connected_and_type_connected()

    def MeasurementAndReport(self, range, verified, error, WireConnection, frequency=None, filter=None) -> None:
        """
            Calculation and reporting function
        """
        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)
        f_result, accuracy = 0, 0
        if not self.TimeDelay:
            self.TimeDelay = 0

#######################################################################################################################
#######################################################  VDC  #########################################################
#######################################################################################################################

        if WireConnection == 'VDC':

#######################################################################################################################
#####################################################  VDC MEAS  ######################################################
#######################################################################################################################

            MOKO.Stage(f'VDC Measure -> range = {range}, verified = {verified}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
            if self.Simulation:
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
            elif self.AutomaticAgilent34460A:
                MOKO.Driver('AgilentDMM', 'set', f'range = {range}')
            else:
                MOKO.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET VDC   ##################################################
            if self.Simulation:
                MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: VDC = {verified}', 'driver')
            elif self.AutomaticFluke5520:
                MOKO.Driver('Fluke5000', 'set', f'VDC = {verified}')
            else:
                MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet VDC = {verified}\nPress OK")
#######################################################################################################################

            while self.ContinueMeasurement:

                time.sleep(self.TimeDelay)
############################################   Agilent34460A READ RESULT    ###########################################
                if self.Simulation:
                    MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                    result = f_verified
                elif self.AutomaticAgilent34460A:
                    result = MOKO.Driver('AgilentDMM', 'get', 'read')
                else:
                    result = MOKO.Messenger("get", "Input result#@notes",
                                            "Enter the measured result from the instrument\nPress OK", "string")
                MOKO.Stage(" ")
#######################################################################################################################

                f_result = MFRT.ConvertStringToFloat(result)
                if isinstance(f_result, str):
                    continue
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error and self.Remeasurement:
                    if self.Count_meas >= self.RemeasurementNumber - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        continue
                else:
                    if accuracy > f_error:
                        self.Status = 'Failed'
                    else:
                        self.Status = 'OK'
                    self.Count_meas = 0

                self.ContinueMeasurement = False

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

        elif WireConnection == 'VAC':

#######################################################################################################################
####################################################  VAC MEAS  #######################################################
#######################################################################################################################

            MOKO.Stage(f'VAC Measure -> range = {range}, verified = {verified}, filter = {filter}, '
                       f'frequency = {frequency}, error = {error}')

#############################################   Agilent34460A SET RANGE   #############################################
############################################   Agilent34460A SET ACBand   #############################################
            if self.Simulation:
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: set >> command: ACBand = {filter}', 'driver')
            elif self.AutomaticAgilent34460A:
                MOKO.Driver('AgilentDMM', 'set', f'range = {range}')
                MOKO.Driver('AgilentDMM', 'set', f'ACBand = {filter}')
            else:
                MOKO.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nSet ACBand = {filter}\nPress OK")

#######################################################################################################################

#############################################   Fluke5520A SET VAC   ##################################################
            if self.Simulation:
                MOKO.Stage(f'DriverSet Fluke5000 >> mode: set >> command: VAC = {verified} {frequency}', 'driver')
            elif self.AutomaticFluke5520:
                MOKO.Driver('Fluke5000', 'set', f'VAC = {verified} {frequency}')
            else:
                MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet VAC = {verified} {frequency}\nPress OK")
#######################################################################################################################

            while self.ContinueMeasurement:

                time.sleep(self.TimeDelay)
############################################   Agilent34460A READ RESULT    ###########################################
                if self.Simulation:
                    MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                    result = f_verified
                elif self.AutomaticAgilent34460A:
                    result = MOKO.Driver('AgilentDMM', 'get', 'read')
                else:
                    result = MOKO.Messenger("get", "Input result#@notes",
                                            "Enter the measured result from the instrument\nPress OK", "string")
                MOKO.Stage(" ")
#######################################################################################################################

                f_result = MFRT.ConvertStringToFloat(result)
                if isinstance(f_result, str):
                    continue
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error and self.Remeasurement:
                    if self.Count_meas >= self.RemeasurementNumber - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        continue
                else:
                    if accuracy > f_error:
                        self.Status = 'Failed'
                    else:
                        self.Status = 'OK'
                    self.Count_meas = 0

                self.ContinueMeasurement = False

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

        elif WireConnection == 'R2':

#######################################################################################################################
####################################################  R2 MEAS  ########################################################
#######################################################################################################################

            MOKO.Stage(f'R2 Measure -> range = {range}, verified = {verified}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
            if self.Simulation:
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
            elif self.AutomaticAgilent34460A:
                MOKO.Driver('AgilentDMM', 'set', f'range = {range}')
            else:
                MOKO.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET R2   ###################################################
            if self.Simulation:
                MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: R2 = {verified}', 'driver')
            elif self.AutomaticFluke5520:
                MOKO.Driver('Fluke5000', 'set', f'R2 = {verified}')
            else:
                MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet R2 = {verified}\nPress OK")
#######################################################################################################################

            while self.ContinueMeasurement:

                time.sleep(self.TimeDelay)
############################################   Agilent34460A READ RESULT    ###########################################
                if self.Simulation:
                    MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                    result = f_verified
                elif self.AutomaticAgilent34460A:
                    result = MOKO.Driver('AgilentDMM', 'get', 'read')
                else:
                    result = MOKO.Messenger("get", "Input result#@notes",
                                            "Enter the measured result from the instrument\nPress OK", "string")
                MOKO.Stage(" ")
#######################################################################################################################

                f_result = MFRT.ConvertStringToFloat(result)
                if isinstance(f_result, str):
                    continue
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error and self.Remeasurement:
                    if self.Count_meas >= self.RemeasurementNumber - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        continue
                else:
                    if accuracy > f_error:
                        self.Status = 'Failed'
                    else:
                        self.Status = 'OK'
                    self.Count_meas = 0

                self.ContinueMeasurement = False

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

        elif WireConnection == 'R4':

#######################################################################################################################
#####################################################  R4 MEAS  #######################################################
#######################################################################################################################

            MOKO.Stage(f'R4 Measure -> range = {range}, verified = {verified}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
            if self.Simulation:
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
            elif self.AutomaticAgilent34460A:
                MOKO.Driver('AgilentDMM', 'set', f'range = {range}')
            else:
                MOKO.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET R4  ###################################################

            if self.Simulation:
                MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: R4 = {verified}', 'driver')
            elif self.AutomaticFluke5520:
                MOKO.Driver('Fluke5000', 'set', f'R4 = {verified}')
            else:
                MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet R4 = {verified}\nPress OK")
#######################################################################################################################

            while self.ContinueMeasurement:

                time.sleep(self.TimeDelay)
############################################   Agilent34460A READ RESULT    ###########################################
                if self.Simulation:
                    MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                    result = f_verified
                elif self.AutomaticAgilent34460A:
                    result = MOKO.Driver('AgilentDMM', 'get', 'read')
                else:
                    result = MOKO.Messenger("get", "Input result#@notes",
                                            "Enter the measured result from the instrument\nPress OK", "string")
                MOKO.Stage(" ")
#######################################################################################################################

                f_result = MFRT.ConvertStringToFloat(result)
                if isinstance(f_result, str):
                    continue
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error and self.Remeasurement:
                    if self.Count_meas >= self.RemeasurementNumber - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        continue
                else:
                    if accuracy > f_error:
                        self.Status = 'Failed'
                    else:
                        self.Status = 'OK'
                    self.Count_meas = 0

                self.ContinueMeasurement = False

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

        elif WireConnection == 'IDC':

#######################################################################################################################
#####################################################  IDC MEAS  ######################################################
#######################################################################################################################

            MOKO.Stage(f'IDC Measure -> range = {range}, verified = {verified}, error = {error}')

############################################   Agilent34460A SET RANGE   ##############################################
            if self.Simulation:
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
            elif self.AutomaticAgilent34460A:
                MOKO.Driver('AgilentDMM', 'set', f'range = {range}')
            else:
                MOKO.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET IDC   ##################################################

            if self.Simulation:
                MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: IDC = {verified}', 'driver')
            elif self.AutomaticFluke5520:
                MOKO.Driver('Fluke5000', 'set', f'IDC = {verified}')
            else:
                MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet IDC = {verified}\nPress OK")
#######################################################################################################################

            while self.ContinueMeasurement:

                time.sleep(self.TimeDelay)
############################################   Agilent34460A READ RESULT    ###########################################
                if self.Simulation:
                    MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                    result = f_verified
                elif self.AutomaticAgilent34460A:
                    result = MOKO.Driver('AgilentDMM', 'get', 'read')
                else:
                    result = MOKO.Messenger("get", "Input result#@notes",
                                            "Enter the measured result from the instrument\nPress OK", "string")
                MOKO.Stage(" ")
#######################################################################################################################

                f_result = MFRT.ConvertStringToFloat(result)
                if isinstance(f_result, str):
                    continue
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error and self.Remeasurement:
                    if self.Count_meas >= self.RemeasurementNumber - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        continue
                else:
                    if accuracy > f_error:
                        self.Status = 'Failed'
                    else:
                        self.Status = 'OK'
                    self.Count_meas = 0

                self.ContinueMeasurement = False

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

        elif WireConnection == 'IAC':

#######################################################################################################################
#####################################################  IAC MEAS  ######################################################
#######################################################################################################################

            MOKO.Stage(f'IAC Measure -> range = {range}, verified = {verified}, filter = {filter}, '
                       f'frequency = {frequency}, error = {error}')

            ############################################   Agilent34460A SET RANGE   ##############################################
            ############################################   Agilent34460A SET ACBand   #############################################
            if self.Simulation:
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: set >> command: ACBand = {filter}', 'driver')
            elif self.AutomaticAgilent34460A:
                MOKO.Driver('AgilentDMM', 'set', f'range = {range}')
                MOKO.Driver('AgilentDMM', 'set', f'ACBand = {filter}')
            else:
                MOKO.Messenger("set", "Make settings on Agilent34460A#@agilent34460a",
                               f"Make settings:\nSet range = {range}\nSet ACBand = {filter}\nPress OK")
#######################################################################################################################

#############################################   Fluke5520A SET IAC   ##################################################

            if self.Simulation:
                MOKO.Stage(f'DriverSet Fluke5000 >> mode: set >> command: IAC = {verified} {frequency}', 'driver')
            elif self.AutomaticFluke5520:
                MOKO.Driver('Fluke5000', 'set', f'IAC = {verified} {frequency}')
            else:
                MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a",
                               f"Make settings:\nSet IAC = {verified} {frequency}\nPress OK")
#######################################################################################################################

            while self.ContinueMeasurement:

                time.sleep(self.TimeDelay)
############################################   Agilent34460A READ RESULT    ###########################################
                if self.Simulation:
                    MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                    result = f_verified
                elif self.AutomaticAgilent34460A:
                    result = MOKO.Driver('AgilentDMM', 'get', 'read')
                else:
                    result = MOKO.Messenger("get", "Input result#@notes",
                                            "Enter the measured result from the instrument\nPress OK", "string")
                MOKO.Stage(" ")
#######################################################################################################################

                f_result = MFRT.ConvertStringToFloat(result)
                if isinstance(f_result, str):
                    continue
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error and self.Remeasurement:
                    if self.Count_meas >= self.RemeasurementNumber - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        continue
                else:
                    if accuracy > f_error:
                        self.Status = 'Failed'
                    else:
                        self.Status = 'OK'
                    self.Count_meas = 0

                self.ContinueMeasurement = False

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
#######################################################################################################################

    def MeasurementStartCommand(self, WireConnection: str) -> None:
        if not self.Driver_start:

############################################   Agilent34460A SET FUNC   ###############################################
            if self.Simulation:
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: func = {WireConnection} ', 'driver')
            elif self.AutomaticAgilent34460A:
                MOKO.Driver('AgilentDMM', 'set', f'func = {WireConnection}')
            else:
                MOKO.Messenger('set', 'Make settings on Agilent34460A#@agilent34460a',
                               f'Make settings:\nSet func = {WireConnection}\nPress OK')
#######################################################################################################################

############################################   Fluke5520 SET OUT = AUX   ##############################################
            if WireConnection in ['IDC', 'IAC']:
                if self.Simulation:
                    MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = AUX', 'driver')
                elif self.AutomaticFluke5520:
                    MOKO.Driver('Fluke5000', 'set', 'OUT = AUX')
                else:
                    MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                                   f'Make settings:\nSet OUT = AUX\nPress OK')
#######################################################################################################################

###########################################   Fluke5520 SET OUT = NORMAL  #############################################
            elif WireConnection != 'R2':
                if self.Simulation:
                    MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = NORMAL', 'driver')
                elif self.AutomaticFluke5520:
                    MOKO.Driver('Fluke5000', 'set', 'OUT = NORMAL')
                else:
                    MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                                   f'Make settings:\nSet OUT = NORMAL\nPress OK')
#######################################################################################################################

############################################   Fluke5520 SET Conn = 4w  ###############################################
            if WireConnection == 'R4':
                if self.Simulation:
                    MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = 4w', 'driver')
                elif self.AutomaticFluke5520:
                    MOKO.Driver('Fluke5000', 'set', 'Conn = 4w')
                else:
                    MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                                   f'Make settings:\nSet Conn = 4w\nPress OK')
#######################################################################################################################

############################################   Fluke5520 SET Conn = NO  ###############################################
            elif WireConnection == 'R2':
                if self.Simulation:
                    MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = NO', 'driver')
                elif self.AutomaticFluke5520:
                    MOKO.Driver('Fluke5000', 'set', 'Conn = NO')
                else:
                    MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                                   f'Make settings:\nSet Conn = NO\nPress OK')
#######################################################################################################################

##########################################   Fluke5520 SET SwitchOFF = DIS   ##########################################
            if self.Simulation:
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = DIS', 'driver')
            elif self.AutomaticFluke5520:
                MOKO.Driver('Fluke5000', 'set', 'SwitchOFF = DISABLE')
            else:
                MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                               f'Make settings:\nSet SwitchOFF = DISABLE\nPress OK')
#######################################################################################################################

            MOKO.Stage(" ")
            self.Driver_start = True

    def MeasurementStopCommand(self) -> None:

########################################   Fluke5520 SET SwitchOFF = ENABLE   #########################################
###############################################   Fluke5520 SET Stop  #################################################
        if self.Simulation:
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = ENABLE', 'driver')
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Stop', 'driver')
        elif self.AutomaticFluke5520:
            MOKO.Driver('Fluke5000', 'set', 'SwitchOFF = ENABLE')
            MOKO.Driver('Fluke5000', 'set', 'Stop')
        else:
            MOKO.Messenger('set', 'Make settings on Fluke5520A#@fluke5520a',
                           f'Make settings:\nSet SwitchOFF = ENABLE\nSet Stop\nPress OK')
#######################################################################################################################

        self.Driver_start = False

    def CheckWireConnection(self, WireConnection: str) -> None:
        self.ContinueMeasurement = True
        if self.WireConnection not in ['VDC', 'VAC', 'R2']:
            if WireConnection == 'VDC':
                MOKO.Messenger('set',
                               'Connecting wires#FLUKE5520A_AGILENT34460A_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check VDC voltage.\n'
                               'Calibrator output NORMAL')
            elif WireConnection == 'VAC':
                MOKO.Messenger('set',
                               'Connecting wires#FLUKE5520A_AGILENT34460A_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check VAC voltage.\n'
                               'Calibrator output NORMAL')
            elif WireConnection == 'R2':
                MOKO.Messenger('set',
                               'Connecting wires#FLUKE5520A_AGILENT34460A_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check R2 resistance.\n'
                               'Calibrator output NORMAL')
        if self.WireConnection not in ['IDC', 'IAC']:
            if WireConnection == 'IDC':
                MOKO.Messenger("set",
                               'Connecting wires#FLUKE5520A_AGILENT34460A_I3_2.jpg',
                               'Connect a multimeter to the calibrator to test.\n'
                               'DC current IDC up to 3 A.\n'
                               'Calibrator output AUX up to 2 A.')
            elif WireConnection == 'IAC':
                MOKO.Messenger("set",
                               'Connecting wires#FLUKE5520A_AGILENT34460A_I3_2.jpg',
                               'Connect a multimeter to the calibrator to test.\n'
                               'AC current IAC up to 3 A.\n'
                               'Calibrator output AUX up to 2 A.')

        if self.WireConnection not in ['R4']:
            if WireConnection == 'R4':     MOKO.Messenger('set',
                                                          'Connecting wires#FLUKE5520A_AGILENT34460A_R4.jpg',
                                                          'Connect a multimeter to the calibrator to check.\n'
                                                          'RES resistance in 4-wire circuit.')

        self.WireConnection = WireConnection
        MOKO.Stage(' ')

    def CheckConnectDevices(self) -> None:
        if self.FirstScriptStart:
            MOKO.Stage('*****************************************************')
            MOKO.Stage('***************** Connect Devices *******************')
            MOKO.Stage('*****************************************************')

            type_setting_agilent = MOKO.Messenger("get", "Choose a way to connect AGILENT34460A#@agilent34460a",
                                                  "Please select an Agilent34460A instrument setup type\n"
                                                  "Attention. By selecting simulation mode, "
                                                  "you run all measurements in simulation mode!!!",
                                                  "choice=Automatic;Manual;Simulation")

            MOKO.Stage(" ")

###############################################   AGILENT34460A Init   ################################################
###########################################   AGILENT34460A SET Timeout  ##############################################
            if type_setting_agilent == 'Automatic':
                self.AutomaticAgilent34460A = True
                choices = None
                self.AGILENT34460A_INIT = MOKO.Driver('AgilentDMM', 'init', '')

                if self.AGILENT34460A_INIT != 'connected':
                    choices = MOKO.Messenger("get", "AGILENT34460A initialization not successful#@agilent34460a",
                                             "Failed to initialize AGILENT34460A. Do you want to continue measuring in "
                                             "Manual mode?", "boolean")

                if not choices or self.AGILENT34460A_INIT == 'connected':
                    MOKO.Driver('AgilentDMM', 'set', 'Timeout = 10000')
                else:
                    self.AutomaticAgilent34460A = False
                    MOKO.Messenger("set", "Make settings Agilent34460A#@agilent34460a", "Make settings:\n"
                                                                                        "Turn on the device\n"
                                                                                        "Set Timeout = 10000\n"
                                                                                        "Press OK")

            elif type_setting_agilent == 'Manual':
                self.AutomaticAgilent34460A = False
                MOKO.Messenger("set", "Make settings Agilent34460A#@agilent34460a", "Make settings:\n"
                                                                                    "Turn on the device\n"
                                                                                    "Set Timeout = 10000\n"
                                                                                    "Press OK")
            else:
                self.Simulation = True
                MOKO.Stage('Driver: AgilentDMM >> mode: init >> command: ', 'driver')
                MOKO.Stage('Driver: AgilentDMM >> mode: set >> command: Timeout = 10000', 'driver')
#######################################################################################################################

            if not self.Simulation:
                type_setting_fluke = MOKO.Messenger("get", "Choose a way to connect FLUKE5520A#@fluke5520a",
                                                    "Please select an FLUKE5520 instrument setup type\n"
                                                    "Attention. By selecting simulation mode, "
                                                    "you run all measurements in simulation mode!!!",
                                                    "choice=Automatic;Manual;Simulation")
            else:
                type_setting_fluke = 'Simulation'
            MOKO.Stage(" ")

###################################################   Fluke5520 Init   ################################################
###############################################   Fluke5520 SET Timeout  ##############################################
################################################   Fluke5520 SET Reset  ###############################################
            if type_setting_fluke == 'Automatic':

                self.AutomaticFluke5520 = True
                choices = None

                self.FLUKE5520A_INIT = MOKO.Driver('Fluke5000', 'init', '')

                if self.FLUKE5520A_INIT != 'connected':
                    choices = MOKO.Messenger("get", "Fluke5520A initialization not successful#@fluke5520a",
                                             "Failed to initialize Fluke5520A. Do you want to continue measuring in "
                                             "Manual mode?", "boolean")
                if not choices or self.FLUKE5520A_INIT == 'connected':
                    MOKO.Driver('Fluke5000', 'set', 'Timeout = 10000')
                    MOKO.Driver('Fluke5000', 'set', 'Reset')
                else:
                    self.AutomaticFluke5520 = False
                    MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a", "Make settings:\n"
                                                                                     "Turn on the device\n"
                                                                                     "Set Timeout = 10000\n"
                                                                                     "Set Reset\n"
                                                                                     "Press OK")

            elif type_setting_fluke == 'Manual':

                self.AutomaticFluke5520 = False
                MOKO.Messenger("set", "Make settings on Fluke5520A#@fluke5520a", "Make settings:\n"
                                                                                 "Turn on the device\n"
                                                                                 "Set Timeout = 10000\n"
                                                                                 "Set Reset\n"
                                                                                 "Press OK")
            else:
                self.Simulation = True
                MOKO.Stage('Driver: Fluke5000 >> mode: init >> command: ', 'driver')
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Timeout = 10000', 'driver')
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Reset', 'driver')
#######################################################################################################################

            self.FirstScriptStart = False

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def CallMessengerChoices(self, verified, error, result, reference_number) -> str:
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

    def CallMessengerErrorPoint(self, verified, error, result, reference_number) -> None:
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

    def SettingMeasurementLimits(self, verified, error) -> None:
        self.LowerLimitResult = verified - error
        self.UpperLimitResult = verified + error

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    @staticmethod
    def LoadTablesHeadInfo() -> None:
        MOKO.Report('VDC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Result#100;"
                                            "Accuracy#100;"
                                            "Permissible error#100;"
                                            "Conclusion#100;")

        MOKO.Report('VAC', 'info', 'table', "Range#100;"
                                            "Point#100;"
                                            "Frequency#100;"
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

        MOKO.Report('IDC', 'info', 'table', "Range#100;"
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
        MOKO.Stage(" ")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def __init_connected_and_type_connected(self):
        type_setting_Fluke5520A = MOKO.Report("TYPE_SETTING_FLUKE5520A", "get", "string", "", 'string')
        type_setting_Agilent34460A = MOKO.Report("TYPE_SETTING_AGILENT34460A", "get", "string", "", 'string')

        if len(type_setting_Agilent34460A) == 0 or len(type_setting_Fluke5520A) == 0:
            self.FirstScriptStart = True
            self.Simulation = False
            return
        else:
            self.FirstScriptStart = False

        if type_setting_Fluke5520A.lower() == 'simulation' or type_setting_Agilent34460A.lower() == 'simulation':
            self.Simulation = True
            return
        else:
            self.Simulation = False

        if type_setting_Fluke5520A.lower() == 'automatic':
            self.AutomaticFluke5520 = True
        else:
            self.AutomaticFluke5520 = False

        if type_setting_Agilent34460A.lower() == 'automatic':
            self.AutomaticAgilent34460A = True
        else:
            self.AutomaticAgilent34460A = False
