import time

import MGPH
import MOKO
import MFRT
import MTLG


class DemoTestIoTMeasurement:

    def __init__(self):
        self.FirstScriptStart, self.FirstResult, self.ContinueMeasurement = True, True, True
        self.WireConnection = None  # [VDC] [IDC]
        self.Count_meas, self.Measurement_start, self.Count_bad_meas = 0, 0, 0
        self.OutCommand, self.GraphInit, self.FailedResult = False, False, False
        self.BK1697B_INIT, self.FY6900_INIT, self.APPA207_INIT = None, None, None
        self.NameGraph = None
        self.ListResult, self.ListValue = [0], [0]
        self.MinError, self.MaxError, self.NumberOfRemeasurementAttempts = 0, 0, 3

    def MeasurementAndReport(self, value, value_limit, wave, amplitude, amplitude_limit, frequency, percent_error,
                             WireConnection, hesh):
        """
            Calculation and reporting function
        """
        name_table = hesh.split('$')[1]

        self.MaxError = float((100 + percent_error) / 100)
        self.MinError = float((100 - percent_error) / 100)

        self.ContinueMeasurement = True

        f_value = MFRT.ConvertStringToFloat(value)

        self.ListValue.append(f_value)

        MOKO.Stage(f"{WireConnection} Measure -> value = {value}, value_limit = {value_limit}, wave = {wave}, "
                   f"amplitude = {amplitude}, amplitude_limit = {amplitude_limit}, frequency = {frequency}, "
                   f"percent_error = {percent_error}")

        while self.ContinueMeasurement:

#######################################################################################################################
#####################################################  VDC  ###########################################################
#######################################################################################################################

            if WireConnection == 'VDC':

#######################################################################################################################
###################################################  VDC MEAS  ########################################################
#######################################################################################################################

                MOKO.Driver('BK1697B', 'set', f'VDC = {value}', 'string')
                MOKO.Driver('FY6900', 'set', f'WAVE = {wave}', 'string')
                MOKO.Driver('FY6900', 'set', f'amplitude = {amplitude}', 'string')
                MOKO.Driver('FY6900', 'set', f'frequency = {frequency}', 'string')
                self.CheckFirstResult()
                result = MOKO.Driver('APPA207', 'get', 'read', 'string')
                MOKO.Stage(" ")
                f_result = MFRT.ConvertStringToFloat(result)
                if f_value * self.MaxError < f_result or f_value * self.MinError > f_result:
                    if self.Count_meas == self.NumberOfRemeasurementAttempts - 1:
                        choices = self.CallMessengerChoices(result=f_result, value=f_value)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(result=f_result, value=f_value)
                        continue
                else:
                    self.FailedResult = False
                    self.Count_meas = 0

                self.ContinueMeasurement = False
                self.ListResult.append(f_result)

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
                MOKO.Stage(" ")

#######################################################################################################################
####################################################  IDC  ############################################################
#######################################################################################################################

            elif WireConnection == 'IDC':

#######################################################################################################################
#################################################  IDC MEAS  ##########################################################`
#######################################################################################################################

                MOKO.Driver('BK1697B', 'set', f'IDC = {value}', 'string')
                MOKO.Driver('FY6900', 'set', f'WAVE = {wave}', 'string')
                MOKO.Driver('FY6900', 'set', f'amplitude = {amplitude}', 'string')
                MOKO.Driver('FY6900', 'set', f'frequency = {frequency}', 'string')
                self.CheckFirstResult()
                result = MOKO.Driver('APPA207', 'get', 'read', 'string')
                MOKO.Stage(" ")
                f_result = MFRT.ConvertStringToFloat(result)
                if f_value * self.MaxError < f_result or f_value * self.MinError > f_result:
                    if self.Count_meas == self.NumberOfRemeasurementAttempts - 1:
                        choices = self.CallMessengerChoices(result=f_result, value=f_value)
                        if choices:
                            continue
                    else:
                        self.CallMessengerErrorPoint(result=f_result, value=f_value)
                        continue
                else:
                    self.FailedResult = False
                    self.Count_meas = 0

                self.ContinueMeasurement = False
                self.ListResult.append(f_result)

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
##################################### Module check wire connection devices #############################################
########################################################################################################################

    def CheckWireConnection(self, WireConnection: str):
        """
            Function check type wire connection
            :param WireConnection: type wire connection
            :return: None
        """
        if self.WireConnection != 'VDC':
            if WireConnection == 'VDC':
                MTLG.TelegramMessenger('beta', 'set', 'Testing VDC', 'Connect a BK1697 to the APPA207 to check '
                                                                     'VDC voltage.\nCalibrator output OUT', 'string')
                MOKO.Messenger('set', 'Testing VDC#TestIoT_VDC.png',
                               'Connect a BK1697 to the APPA207 to check VDC voltage.\n'
                               'Calibrator output OUT')
        if self.WireConnection != "IDC":
            if WireConnection == 'IDC':
                MTLG.TelegramMessenger('beta', 'set', 'Testing IDC', 'Connect a BK1697 to the APPA207 to check '
                                                                     'IDC currency.\nCalibrator output OUT', 'string')
                MOKO.Messenger('set', 'Testing IDC#TestIoT_IDC.png',
                               'Connect a BK1697 to the APPA207 to check IDC currency.\n'
                               'Calibrator output OUT')

        self.WireConnection = WireConnection
        MOKO.Stage(' ')

########################################################################################################################
################################### Module check number result: first or no ############################################
########################################################################################################################

    def CheckFirstResult(self):
        """
            Function checked a first result in block
            :return: None
        """
        if self.FirstResult:
            time.sleep(1)

########################################################################################################################
############################################# Module connected devices #################################################
########################################################################################################################

    def CheckConnectDevices(self):
        while self.BK1697B_INIT != 'connected':
            MOKO.Stage("*********************************************************")
            MOKO.Stage("**************** Init devices BK1697B *******************")
            MOKO.Stage("*********************************************************")
            self.BK1697B_INIT = MOKO.Driver('BK1697B', 'init', '', 'string')
            MOKO.Stage(" ")

        while self.FY6900_INIT != 'connected':
            MOKO.Stage("*********************************************************")
            MOKO.Stage("***************** Init devices FY6900 *******************")
            MOKO.Stage("*********************************************************")
            self.FY6900_INIT = MOKO.Driver('FY6900', 'init', '', 'string')
            MOKO.Stage(" ")

        while self.APPA207_INIT != 'connected':
            MOKO.Stage("*********************************************************")
            MOKO.Stage("**************** Init devices APPA207 *******************")
            MOKO.Stage("*********************************************************")
            self.APPA207_INIT = MOKO.Driver('APPA207', 'init', '', 'string')
            MOKO.Stage(" ")

########################################################################################################################
########################################### Module for working with Graph ##############################################
########################################################################################################################

    def CheckGraphInit(self):
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

    def CreateGraph(self):
        """
            Function initialization functions create a Graph
            :return: None
        """
        self.CreateGraphValue()
        self.CreateGraphResult()
        self.FirstResult = False

    def CreateGraphMask(self, value_limit):
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

    def CreateGraphValue(self):
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
        ArrOy_plus = [float(f'{x * self.MaxError:.10f}') for x in self.ListValue]
        ArrOy_minus = [float(f'{x * self.MinError:10f}') for x in self.ListValue]
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

    def CreateGraphResult(self):
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

    def GetScreenshot(self):
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
        MOKO.Stage(" ")

########################################################################################################################
################################### Module driver BK1697B set output ON or OFF #########################################
########################################################################################################################

    def OutONNCommand(self):
        """
            BK1697B output check function ON
            :return: None
        """
        if not self.OutCommand:
            self.OutCommand = True
            MOKO.Driver('BK1697B', 'set', 'OUTPUT = ON', 'string')
            MOKO.Stage(" ")

    def OutOFFCommand(self):
        """
            BK1697B output set function OUT
            :return: None
        """
        self.OutCommand = False
        self.FirstResult = True
        MOKO.Driver('BK1697B', 'set', 'OUTPUT = OFF', 'string')

########################################################################################################################
###################################### Module repeat or error report ###################################################
########################################################################################################################

    def CallMessengerChoices(self, result, value) -> str:

        limit_type = "upper" if self.MaxError * value < result else "lower"
        limit_value = result - self.MaxError * value if limit_type == "upper" else self.MinError * value

        error_message = 'Do you want to repeat measuring this point?\n'
        error_message += f'Lower limit < Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.MinError * value, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.MaxError * value, resolution=3)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, resolution=3)}'

        choices = MOKO.Messenger('get', 'The measurement result did not pass the specified limit#@repeat',
                                 error_message, 'boolean')

        self.FailedResult = True
        self.Count_meas = 0
        return choices

    def CallMessengerErrorPoint(self, result, value) -> None:

        limit_type = "upper" if self.MaxError * value < result else "lower"
        limit_value = result - self.MaxError * value if limit_type == "upper" else self.MinError * value

        error_message = 'The measurement result did not pass the specified limit\n'
        error_message += 'The value is being remeasured\n'
        error_message += f'Lower limit <  Result < Upper limit\n'
        error_message += f'{MFRT.ConvertFloatToString(self.MinError * value, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(result, resolution=3)} < '
        error_message += f'{MFRT.ConvertFloatToString(self.MaxError * value, resolution=3)}\n'
        error_message += f'The measurement does not meet the {limit_type} limit ' \
                         f'on {MFRT.ConvertFloatToString(limit_value, resolution=3)}'

        MOKO.Messenger('set', 'Measurement failed#@failed', error_message, delaytime='5')
        self.Count_meas += 1


########################################################################################################################
######################################## Module load tables in MOKO.Reports ############################################
########################################################################################################################

    @staticmethod
    def LoadTablesHeadInfo():
        MOKO.Report('VDC_SIN', 'info', 'table', "Value#100;"
                                                "ValueLimit#100;"
                                                "PercentError#100;"
                                                "PermissibleVariation#150;"
                                                "Wave#100;"
                                                "Amplitude#100;"
                                                "AmplitudeLimit#100;"
                                                "Frequency#100;"
                                                "Result#100;")

        MOKO.Report('VDC_SQUARE', 'info', 'table', "Value#100;"
                                                   "ValueLimit#100;"
                                                   "PercentError#100;"
                                                   "PermissibleVariation#150;"
                                                   "Wave#100;"
                                                   "Amplitude#100;"
                                                   "AmplitudeLimit#100;"
                                                   "Frequency#100;"
                                                   "Result#100;")

        MOKO.Report('VDC_RECTANGLE', 'info', 'table', "Value#100;"
                                                      "ValueLimit#100;"
                                                      "PercentError#100;"
                                                      "PermissibleVariation#150;"
                                                      "Wave#100;"
                                                      "Amplitude#100;"
                                                      "AmplitudeLimit#100;"
                                                      "Frequency#100;"
                                                      "Result#100;")

        MOKO.Report('VDC_TRAPEZOID', 'info', 'table', "Value#100;"
                                                      "ValueLimit#100;"
                                                      "PercentError#100;"
                                                      "PermissibleVariation#150;"
                                                      "Wave#100;"
                                                      "Amplitude#100;"
                                                      "AmplitudeLimit#100;"
                                                      "Frequency#100;"
                                                      "Result#100;")

        MOKO.Report('IDC_CMOS', 'info', 'table', "Value#100;"
                                                 "ValueLimit#100;"
                                                 "PercentError#100;"
                                                 "PermissibleVariation#150;"
                                                 "Wave#100;"
                                                 "Amplitude#100;"
                                                 "AmplitudeLimit#100;"
                                                 "Frequency#100;"
                                                 "Result#100;")

        MOKO.Report('IDC_PULSE', 'info', 'table', "Value#100;"
                                                  "ValueLimit#100;"
                                                  "PercentError#100;"
                                                  "PermissibleVariation#150;"
                                                  "Wave#100;"
                                                  "Amplitude#100;"
                                                  "AmplitudeLimit#100;"
                                                  "Frequency#100;"
                                                  "Result#100;")

        MOKO.Report('IDC_RAMP', 'info', 'table', "Value#100;"
                                                 "ValueLimit#100;"
                                                 "PercentError#100;"
                                                 "PermissibleVariation#150;"
                                                 "Wave#100;"
                                                 "Amplitude#100;"
                                                 "AmplitudeLimit#100;"
                                                 "Frequency#100;"
                                                 "Result#100;")

        MOKO.Report('IDC_NEGRAMP', 'info', 'table', "Value#100;"
                                                    "ValueLimit#100;"
                                                    "PercentError#100;"
                                                    "PermissibleVariation#150;"
                                                    "Wave#100;"
                                                    "Amplitude#100;"
                                                    "AmplitudeLimit#100;"
                                                    "Frequency#100;"
                                                    "Result#100;")
        MOKO.Stage(" ")


Testing = DemoTestIoTMeasurement()
