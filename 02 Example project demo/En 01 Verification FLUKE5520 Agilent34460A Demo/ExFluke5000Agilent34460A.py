import time
import MOKO
import MFRT


class ExFluke5000Agilent34460A:
    def __init__(self) -> None:
        self.FirstScriptStart = True
        self.NumberOfRemeasurementAttempts = 3
        self.WireConnection = str
        self.Driver_start = False
        self.Count_meas = 0
        self.ListConstResult = list()
        self.Status = None
        self.ContinueMeasurement = True
        self.LowerLimitResult, self.UpperLimitResult = None, None

    def MeasurementAndReport(self, range, verified, error, WireConnection, frequency=None, filter=None) -> None:
        """
            Calculation and reporting function
        """
        f_verified = MFRT.ConvertStringToFloat(verified)
        f_error = MFRT.ConvertStringToFloat(error)

        while self.ContinueMeasurement is True:
#######################################################################################################################
#######################################################  VDC  #########################################################
#######################################################################################################################

            if WireConnection == 'VDC':

#######################################################################################################################
#####################################################  VDC MEAS  ######################################################
#######################################################################################################################

                MOKO.Stage(f'VDC Measure -> range = {range}, verified = {verified}, error = {error}')
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: VDC = {verified}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                result = f_verified * 1.00000001
                MOKO.Stage(" ")
                f_result = MFRT.ConvertStringToFloat(result)
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error:
                    if self.Count_meas == self.NumberOfRemeasurementAttempts - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        continue
                else:
                    self.Count_meas = 0
                    self.Status = 'OK'

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
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: set >> command: ACBand = {filter}', 'driver')
                MOKO.Stage(f'DriverSet Fluke5000 >> mode: set >> command: VAC = {verified} {frequency}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                result = f_verified * 1.00000001
                MOKO.Stage(" ")
                f_result = MFRT.ConvertStringToFloat(result)
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error:
                    if self.Count_meas == self.NumberOfRemeasurementAttempts - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        continue
                else:
                    self.Count_meas = 0
                    self.Status = 'OK'

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
#######################################################   R2  #########################################################
#######################################################################################################################

            elif WireConnection == 'R2':

#######################################################################################################################
######################################################  R2 MEAS  ######################################################
#######################################################################################################################

                MOKO.Stage(f'R2 Measure -> range = {range}, verified = {verified}, error = {error}')
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: R2 = {verified}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                result = f_verified * 1.00000001
                MOKO.Stage(" ")
                f_result = MFRT.ConvertStringToFloat(result)
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error:
                    if self.Count_meas == self.NumberOfRemeasurementAttempts - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        continue
                else:
                    self.Count_meas = 0
                    self.Status = 'OK'

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
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: R4 = {verified}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                result = f_verified * 1.00000001
                MOKO.Stage(" ")
                f_result = MFRT.ConvertStringToFloat(result)
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error:
                    if self.Count_meas == self.NumberOfRemeasurementAttempts - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        continue
                else:
                    self.Count_meas = 0
                    self.Status = 'OK'

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
                MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                MOKO.Stage(f'Driver: Fluke5000 >> mode: set >> command: IDC = {verified}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                result = f_verified * 1.00000001
                MOKO.Stage(" ")
                f_result = MFRT.ConvertStringToFloat(result)
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error:
                    if self.Count_meas == self.NumberOfRemeasurementAttempts - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=result, reference_number=verified)
                        continue
                else:
                    self.Count_meas = 0
                    self.Status = 'OK'

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
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: set >> command: range = {range}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: set >> command: ACBand = {filter}', 'driver')
                MOKO.Stage(f'DriverSet Fluke5000 >> mode: set >> command: IAC = {verified} {frequency}', 'driver')
                MOKO.Stage(f'DriverSet AgilentDMM >> mode: get >> command: result = read', 'driver')
                result = f_verified * 1.00000001
                MOKO.Stage(" ")
                f_result = MFRT.ConvertStringToFloat(result)
                accuracy = abs(f_verified - f_result)
                if accuracy > f_error:
                    if self.Count_meas == self.NumberOfRemeasurementAttempts - 1:
                        choices = self.CallMessengerChoices(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(
                            verified=f_verified, error=f_error, result=f_result, reference_number=verified)
                        continue
                else:
                    self.Count_meas = 0
                    self.Status = 'OK'

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

            MOKO.Stage(f'Driver: AgilentDMM >> mode: set >> command: func = {WireConnection} ', 'driver')

            if WireConnection in ['IDC', 'IAC']:
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = AUX', 'driver')
            elif WireConnection != 'R2':
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: OUT = NORMAL', 'driver')

            if WireConnection == 'R4':
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = 4w', 'driver')
            elif WireConnection == 'R2':
                MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Conn = NO', 'driver')

            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = DISABLE', 'driver')
            MOKO.Stage(" ")
            self.Driver_start = True

    def MeasurementStopCommand(self) -> None:
        MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: SwitchOFF = ENABLE', 'driver')
        MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Stop', 'driver')
        self.Driver_start = False

    def CheckWireConnection(self, WireConnection: str) -> None:
        self.ContinueMeasurement = True
        if self.WireConnection not in ['VDC', 'VAC', 'R2']:
            if WireConnection == 'VDC':
                MOKO.Messenger('set',
                               'Connecting wires#FLUKE5520_AGILENT34460_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check VDC voltage.\n'
                               'Calibrator output NORMAL')
            elif WireConnection == 'VAC':
                MOKO.Messenger('set',
                               'Connecting wires#FLUKE5520_AGILENT34460_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check VAC voltage.\n'
                               'Calibrator output NORMAL')
            elif WireConnection == 'R2':
                MOKO.Messenger('set',
                               'Connecting wires#FLUKE5520_AGILENT34460_V_R2.jpg',
                               'Connect a multimeter to the calibrator to check R2 resistance.\n'
                               'Calibrator output NORMAL')
        if self.WireConnection not in ['IDC', 'IAC']:
            if WireConnection == 'IDC':
                MOKO.Messenger("set",
                               'Connecting wires#FLUKE5520_AGILENT34460_I3_2.jpg',
                               'Connect a multimeter to the calibrator to test.\n'
                               'DC current IDC up to 3 A.\n'
                               'Calibrator output AUX up to 2 A.')
            elif WireConnection == 'IAC':
                MOKO.Messenger("set",
                               'Connecting wires#FLUKE5520_AGILENT34460_I3_2.jpg',
                               'Connect a multimeter to the calibrator to test.\n'
                               'AC current IAC up to 3 A.\n'
                               'Calibrator output AUX up to 2 A.')

        if self.WireConnection not in ['R4']:
            if WireConnection == 'R4':     MOKO.Messenger('set',
                                                          'Connecting wires#FLUKE5520_AGILENT34460_R4.jpg',
                                                          'Connect a multimeter to the calibrator to check.\n'
                                                          'RES resistance in 4-wire circuit.')

        self.WireConnection = WireConnection
        MOKO.Stage(' ')

    def CheckConnectDevices(self) -> None:
        if self.FirstScriptStart:
            MOKO.Stage('*****************************************************')
            MOKO.Stage('***************** Connect Devices *******************')
            MOKO.Stage('*****************************************************')
            MOKO.Stage('Driver: AgilentDMM >> mode: set >> command: Timeout = 10000', 'driver')
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Timeout = 10000', 'driver')
            MOKO.Stage('Driver: Fluke5000 >> mode: set >> command: Reset', 'driver')
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
