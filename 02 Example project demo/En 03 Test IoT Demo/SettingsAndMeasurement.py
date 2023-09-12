import time

import MGPH
import MOSC
import MOKO
import MFRT
import MTLG
from APPA207 import APPA207
from BK1697B import BK1697B
from FY6900 import FY6900


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


class DemoTestIoTMeasurement:

    def __init__(self):
        self.FirstScriptStart, self.FirstResult, self.ContinueMeasurement = True, True, True
        self.WireConnection, self.NameGraph, self.Status = str(), str(), str()
        self.TimeDelay, self.Count_meas, self.RemeasurementNumber = 0, 0, 0
        self.OutCommand, self.GraphInit, self.FailedResult, self.Remeasurement = False, False, False, False
        self.ListResult, self.ListValue = [0], [0]
        self.MinError, self.MaxError = 0, 0
        self.APPA207 = APPA207()
        self.BK1697B = BK1697B()
        self.FY6900 = FY6900()
        self.__init_connected_and_type_connected()


#######################################################################################################################
#####################################################  VDC  ###########################################################
#######################################################################################################################

    def VDC_Measurement(
            self,
            value: (str | float | int),
            value_limit: (str | float | int),
            percent_error: (float | int),
            wave: str,
            amplitude: (str | float | int),
            amplitude_limit: int,
            frequency: (str | float | int),
            hesh: str,

    ) -> None:

        name_table = self.__init_measurement(hesh=hesh, percent_error=percent_error)

        f_value = MFRT.ConvertStringToFloat(value)

        self.ListValue.append(f_value)

        MOKO.Stage(f"VDC Measure -> value = {value}, value_limit = {value_limit}, wave = {wave}, "
                   f"amplitude = {amplitude}, amplitude_limit = {amplitude_limit}, frequency = {frequency}, "
                   f"percent_error = {percent_error}")



#######################################################################################################################
###################################################  VDC MEAS  ########################################################
#######################################################################################################################

        self.BK1697B.SET_VALUE(value=value, Wireconnection='VDC')

        self.FY6900.SET_WAVE(wave=wave)
        self.FY6900.SET_AMPLITUDE(amplitude=amplitude)
        self.FY6900.SET_FREQUENCY(frequency=frequency)

        result = self.GetResultMeasurent(value=f_value)

#######################################################################################################################
##################################################  VDC REPORT  #######################################################
#######################################################################################################################

        MOKO.Report(name_table, "set", "table", f"{value};"
                                                f"{value_limit};"
                                                f"{percent_error};"
                                                f"{MFRT.ConvertFloatToString(value * (percent_error / 100), resolution=3)};"
                                                f"{wave};"
                                                f"{amplitude};"
                                                f"{amplitude_limit};"
                                                f"{frequency};"
                                                f"{result};")

#######################################################################################################################
#################################################  IDC MEAS  ##########################################################`
#######################################################################################################################

    def IDC_MEASUREMENT(
            self,
            value: (str | float | int),
            value_limit: (str | float | int),
            percent_error: (float | int),
            wave: str,
            amplitude: (str | float | int),
            amplitude_limit: int,
            frequency: (str | float | int),
            hesh: str,

    ) -> None:

        name_table = self.__init_measurement(hesh=hesh, percent_error=percent_error)

        f_value = MFRT.ConvertStringToFloat(value)

        self.ListValue.append(f_value)

        MOKO.Stage(f"IDC Measure -> value = {value}, value_limit = {value_limit}, wave = {wave}, "
                   f"amplitude = {amplitude}, amplitude_limit = {amplitude_limit}, frequency = {frequency}, "
                   f"percent_error = {percent_error}")

        self.BK1697B.SET_VALUE(value=value, Wireconnection='IDC')

        self.FY6900.SET_WAVE(wave=wave)
        self.FY6900.SET_AMPLITUDE(amplitude=amplitude)
        self.FY6900.SET_FREQUENCY(frequency=frequency)

        result = self.GetResultMeasurent(value=f_value)

#######################################################################################################################
####################################################  IDC REPORT  #####################################################
#######################################################################################################################

        MOKO.Report(name_table, "set", "table", f"{value};"
                                                f"{value_limit};"
                                                f"{percent_error};"
                                                f"{MFRT.ConvertFloatToString(f_value * (percent_error / 100), resolution=3)};"
                                                f"{wave};"
                                                f"{amplitude};"
                                                f"{amplitude_limit};"
                                                f"{frequency};"
                                                f"{result};")

        MOKO.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################  Module return result measurement  ############################################
########################################################################################################################
########################################################################################################################
    def GetResultMeasurent(self, value: (float | int)) -> float:

        f_result, result = 0, 0
        while self.ContinueMeasurement:
            time.sleep(self.TimeDelay)

            result = self.APPA207.READ_RESULT(value=value)

            f_result = MFRT.ConvertStringToFloat(result)

            if isinstance(f_result, str):
                continue

            if value * self.MaxError < f_result or value * self.MinError > f_result:
                if self.Count_meas >= self.RemeasurementNumber - 1:
                    choices = self.CallMessengerChoices(result=f_result, value=value)
                    if choices:
                        continue
                else:
                    self.CallMessengerErrorPoint(result=f_result, value=value)
                    continue
            else:
                if value * self.MaxError < f_result or value * self.MinError > f_result:
                    self.Status = 'Failed'
                else:
                    self.Status = 'OK'
                self.Count_meas = 0
            self.ContinueMeasurement = False
        self.ListResult.append(f_result)
        return result

########################################################################################################################
########################################################################################################################
##################################### Module check wire connection devices #############################################
########################################################################################################################
########################################################################################################################

    def CheckWireConnection(self, WireConnection: str) -> None:

        """
            Function check type wire connection
            :param WireConnection: type wire connection
            :return: None
        """
        if self.WireConnection != WireConnection:
            match WireConnection:
                case "VDC":
                    MTLG.TelegramMessenger('beta', 'set', 'Testing VDC', 'Connect a BK1697 to the APPA207 to check '
                                                                         'VDC voltage.\nCalibrator output OUT', 'string')
                    MOKO.Messenger('set', 'Testing VDC#TestIoT_VDC.png',
                                   'Connect a BK1697 to the APPA207 to check VDC voltage.\n'
                                   'Calibrator output OUT')

                case "IDC":
                    MTLG.TelegramMessenger('beta', 'set', 'Testing IDC', 'Connect a BK1697 to the APPA207 to check '
                                                                         'IDC currenty.\nCalibrator output OUT', 'string')
                    MOKO.Messenger('set', 'Testing IDC#TestIoT_IDC.png',
                                   'Connect a BK1697 to the APPA207 to check IDC currenty.\n'
                                   'Calibrator output OUT')

            self.WireConnection = WireConnection
            MOKO.Stage(' ')

########################################################################################################################
########################################################################################################################
############################################# Module connected devices #################################################
########################################################################################################################
########################################################################################################################

    def CheckConnectDevices(self) -> None:

        if self.FirstScriptStart:
            self.BK1697B.Initialization(init=False)
            self.FY6900.Initialization(init=False)
            self.APPA207.Initialization(init=False)
            self.BK1697B.SET_OUTPUT_OFF()
            self.FirstScriptStart = False


########################################################################################################################
########################################################################################################################
########################################### Module for working with Graph ##############################################
########################################################################################################################
########################################################################################################################

    def CheckGraphInit(self) -> None:
        """
            Function check initialization Graph
            :return: None
        """
        if not self.GraphInit:
            MOKO.Stage("*********************************************************")
            MOKO.Stage("***************** Init module Graph   *******************")
            MOKO.Stage("*********************************************************")
            MOKO.Stage(" ")
            MGPH.GraphInit()
            self.GraphInit = True
            time.sleep(5)
            MOKO.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraph(self) -> None:
        """
            Function initialization functions create a Graph
            :return: None
        """
        self.CreateGraphValue()
        self.CreateGraphResult()
        self.FirstResult = False

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphMask(self, value_limit: int) -> None:
        """
            Create mask Graph
            :param value_limit: coordinate value Ox
            :return: None
        """
        if self.FirstResult:
            MOKO.Stage("*********************************************************")
            MOKO.Stage("***************** Create Graph mask  ********************")
            MOKO.Stage("*********************************************************")
            MOKO.Stage(" ")
            MGPH.ClearGraph()
            Value_OyOx = [0, value_limit, 0, 20]
            Name_Oy = "Amplitude"
            Name_Ox = " Iteration"
            Autoscale = "No"
            MGPH.AddGraphSett(Value_OyOx, Name_Oy, Name_Ox, Autoscale)
            MOKO.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CreateGraphValue(self) -> None:
        """
            Function to create a Graph by value
            :return: None
        """
        MOKO.Stage("*********************************************************")
        MOKO.Stage("************* Create Graph a input value ****************")
        MOKO.Stage("*********************************************************")
        MOKO.Stage(" ")
        name_graph_plus = f'{self.NameGraph}_value_plus'
        name_graph_minus = f'{self.NameGraph}_value_minus'
        ArrOy_plus = [float(f'{x * self.MaxError:.14f}') for x in self.ListValue]
        ArrOy_minus = [float(f'{x * self.MinError:14f}') for x in self.ListValue]
        numLine_plus = name_graph_plus
        numLine_minus = name_graph_minus
        ArrOx = [x for x in range(len(self.ListValue))]
        LineWidth = "3"
        Color = "FF0000"
        Visible = "Yes"
        if self.FirstResult:
            MGPH.AddLine(name_graph_plus, ArrOy_plus, ArrOx, LineWidth, Color, Visible)
            MGPH.AddLine(name_graph_minus, ArrOy_minus, ArrOx, LineWidth, Color, Visible)
        else:
            MGPH.ChangeLine(numLine_plus, name_graph_plus, ArrOy_plus, ArrOx, LineWidth, Color, Visible)
            MGPH.ChangeLine(numLine_minus, name_graph_minus, ArrOy_minus, ArrOx, LineWidth, Color, Visible)
        MOKO.Stage(" ")

########################################################################################################################
########################################################################################################################
#######################################################################################################################

    def CreateGraphResult(self) -> None:
        """
            Function to create a Graph by result
            :return: None
        """
        MOKO.Stage("*********************************************************")
        MOKO.Stage("************* Create Graph a result value ***************")
        MOKO.Stage("*********************************************************")
        MOKO.Stage(" ")
        name = f'{self.NameGraph}_result'
        numLine = name
        ArrOy = self.ListResult
        ArrOx = [x for x in range(len(self.ListResult))]
        LineWidth = "3"
        Color = "0"
        Visible = "Yes"
        if self.FirstResult:
            MGPH.AddLine(name, ArrOy, ArrOx, LineWidth, Color, Visible)
        else:
            MGPH.ChangeLine(numLine, name, ArrOy, ArrOx, LineWidth, Color, Visible)

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def GetScreenshot(self) -> None:
        """
            Function create screenshot Graph, save screenshot in Word and clear Graph
            :return: None
        """
        MOKO.Stage("*********************************************************")
        MOKO.Stage("************* Getting a screenshot Graph ****************")
        MOKO.Stage("*********************************************************")
        MOKO.Stage(" ")
        screen = MGPH.GetScreenshotGraph()
        MOKO.Stage(f"name: {self.NameGraph} >> mode: set >> kind: picture >> data: screen", "Report")
        MOKO.Stage(" ")
        MOKO.Report(self.NameGraph, 'set', 'picture', screen)
        self.NameGraph = None
        MGPH.ClearGraph()
        self.ListValue, self.ListResult = [0], [0]
        self.FirstResult = True
        MOKO.Stage(" ")


########################################################################################################################
########################################################################################################################
###################################### Module repeat or error report ###################################################
########################################################################################################################
########################################################################################################################

    def CallMessengerChoices(self, result: (float | int), value: (float | int)) -> str:

        limit_type = "upper" if self.MaxError * value < result else "lower"
        limit_value = result - (self.MaxError * value) if limit_type == "upper" else self.MinError * value - result

        error_message = 'Do you want to repeat measuring this point?\n'
        error_message += f'Lower limit < Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.MinError * value, resolution=3) if self.MinError * value > 0 else MFRT.ConvertFloatToString(0, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.MaxError * value, resolution=3)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, resolution=3)}'

        choices = MOKO.Messenger('get', 'The measurement result did not pass the specified limit#@repeat',
                                 error_message, 'boolean')

        self.FailedResult = True
        self.Count_meas = 0
        return choices

########################################################################################################################
########################################################################################################################
########################################################################################################################

    def CallMessengerErrorPoint(self, result: (float | int), value: (float | int)) -> None:

        limit_type = "upper" if self.MaxError * value < result else "lower"
        limit_value = result - (self.MaxError * value) if limit_type == "upper" else self.MinError * value - result
        error_message = 'The measurement result did not pass the specified limit\n'
        error_message += 'The value is being remeasured\n'
        error_message += f'Lower limit <  Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.MinError * value, resolution=3) if self.MinError * value > 0 else MFRT.ConvertFloatToString(0, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.MaxError * value, resolution=3)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, resolution=3)}'

        MOKO.Messenger('set', 'Measurement failed#@failed', error_message, delaytime='5')
        self.Count_meas += 1

########################################################################################################################
########################################################################################################################
######################################## Module load tables in MOKO.Reports ############################################
########################################################################################################################
########################################################################################################################

    @staticmethod
    def LoadTablesHeadInfo(number_wave: int) -> None:
        wave_array = ["VDC_SIN", "VDC_SQUARE", "VDC_RECTANGLE", "VDC_TRAPEZOID", "IDC_CMOS", "IDC_PULSE", "IDC_RAMP",
                      "IDC_NEGRAMP"]
        if number_wave < 1:
            number_wave = 1
        elif number_wave > 8:
            number_wave = 8
        elif number_wave == 4:
            wave_array = ["VDC_SIN", "VDC_SQUARE", "IDC_RAMP", "IDC_NEGRAMP"]
        for count in range(number_wave):
            MOKO.Report(f'{wave_array[count]}', 'info', 'table', "Value#100;"
                        "ValueLimit#100;"
                        "PercentError#100;"
                        "PermissibleVariation#150;"
                        "Wave#100;"
                        "Amplitude#100;"
                        "AmplitudeLimit#100;"
                        "Frequency#100;"
                        "Result#100;")

        MOKO.Stage(" ")

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

    def __init_measurement(self, hesh: str, percent_error: (int | float)):
        name_table = hesh.split('$')[1]

        self.MaxError = float((100 + percent_error) / 100)
        self.MinError = float((100 - percent_error) / 100)

        self.ContinueMeasurement = True

        return name_table

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

    def __init_connected_and_type_connected(self) -> None:
        type_setting_BK1697B = MOKO.Report("TYPE_SETTING_BK1697B", "get", "string", "", 'string')
        type_setting_FY6900 = MOKO.Report("TYPE_SETTING_FY6900", "get", "string", "", 'string')
        type_setting_APPA207 = MOKO.Report("TYPE_SETTING_APPA207", "get", "string", "", 'string')

        if len(type_setting_BK1697B) == 0 or len(type_setting_FY6900) == 0 or len(type_setting_APPA207) == 0:
            self.FirstScriptStart = True
            return
        else:
            self.FirstScriptStart = False

        if type_setting_BK1697B == 'Automatic':
            self.BK1697B.IsAutomatic = True
        else:
            self.BK1697B.IsAutomatic = False

        if type_setting_FY6900 == 'Automatic':
            self.FY6900.IsAutomatic = True
        else:
            self.FY6900.IsAutomatic = False

        if type_setting_APPA207 == 'Automatic':
            self.APPA207.IsAutomatic = True
        else:
            self.APPA207.IsAutomatic = False


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

Testing = DemoTestIoTMeasurement()
