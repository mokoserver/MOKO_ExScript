import MOKO
from MOSC import Heshstatus, hesh_passed, hesh_failed
from Real_Test_DC_DC_Converter import Testing
import MTLG
MTLG.TelegramProgram('alpha', 'Measurement script', 'set', 'init', 'string')
MOKO.Stage("*********************************************************")
MOKO.Stage("****************** Measurement script *******************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")
MOKO.Stage("*********************************************************")
MOKO.Stage('**************** Null flags of system ****************')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")
Testing.LoadTablesHeadInfo()
Testing.SET_OUTPUT_OFF()


def VDC(
        value: (str | float | int),
        range_value: (str | float | int),
        allowable_stabilization_factor: (float | int),
        is_operating_range: bool,
        hesh: str,
        time_delay: (float | int) = 0.0

) -> None:

    if Heshstatus(hesh):

        Testing.CheckConnectDevices()

        Testing.CheckWireConnection(WireConnection='VDC')

        Testing.OutONNCommand()
        Testing.CheckGraphInit()
        Testing.CreateGraphMask(range_value=range_value)

        Testing.TimeDelay = time_delay

        Testing.MeasurementAndReport(value=value, range_value=range_value, is_operating_range=is_operating_range,
                                     allowable_stabilization_factor=allowable_stabilization_factor, hesh=hesh,
                                     WireConnection='VDC')

        Testing.CreateGraph(WireConnection='VDC')

        if Testing.status == 'Failed':
            hesh_failed()
        else:
            hesh_passed()


def IDC(
        value: (str | float | int),
        range_value: (str | float | int),
        allowable_stabilization_factor: (float | int),
        is_operating_range: bool,
        hesh: str,
        time_delay: (int, float) = 0.0

) -> None:

    if Heshstatus(hesh):

        Testing.CheckConnectDevices()

        Testing.CheckWireConnection(WireConnection='IDC')

        Testing.OutONNCommand()
        Testing.CheckGraphInit()
        Testing.CreateGraphMask(range_value=range_value)

        Testing.TimeDelay = time_delay

        Testing.MeasurementAndReport(value=value, range_value=range_value, is_operating_range=is_operating_range,
                                     allowable_stabilization_factor=allowable_stabilization_factor, hesh=hesh, 
                                     WireConnection='IDC')

        Testing.CreateGraph(WireConnection='IDC')

        if Testing.status == 'Failed':
            hesh_failed()
        else:
            hesh_passed()

#region Voltage measurement$VDC
#description: value \nmeasurement, V;range value, V;allowable\nstabilization\nfactor;is operating\nrange,\nTrue or False;delay time \nbefore \nmeasurement, s;
MOKO.Program('tree', 'set', 'select = Voltage measurement$VDC')

MOKO.Stage('Set NameGraph => VDC_GRAPH')
Testing.NameGraph = 'VDC_GRAPH'
MOKO.Stage(" ")

VDC(value=1,   range_value=40, allowable_stabilization_factor=0,   is_operating_range=False, time_delay=3, hesh='Meas 1$VDC')   #hesh Meas 1$VDC:   1  ;40  ;0    ;False;3.000
VDC(value=1,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 2$VDC')   #hesh Meas 2$VDC:   1  ;40  ;0.1  ;False;3.000
VDC(value=2,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 3$VDC')   #hesh Meas 3$VDC:   2  ;40  ;0.1  ;False;3.000
VDC(value=3,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 4$VDC')   #hesh Meas 4$VDC:   3  ;40  ;0.1  ;False;3.000
VDC(value=4,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 5$VDC')   #hesh Meas 5$VDC:   4  ;40  ;0.1  ;False;3.000
VDC(value=5,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 6$VDC')   #hesh Meas 6$VDC:   5  ;40  ;0.1  ;False;3.000
VDC(value=6,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 7$VDC')   #hesh Meas 7$VDC:   6  ;40  ;0.1  ;False;3.000
VDC(value=7,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 8$VDC')   #hesh Meas 8$VDC:   7  ;40  ;0.1  ;False;3.000
VDC(value=8,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 9$VDC')   #hesh Meas 9$VDC:   8  ;40  ;0.1  ;False;3.000
VDC(value=9,   range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 10$VDC')  #hesh Meas 10$VDC:  9  ;40  ;0.1  ;False;3.000
VDC(value=10,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 11$VDC')  #hesh Meas 11$VDC:  10 ;40  ;0.1  ;True ;3.000
VDC(value=11,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 12$VDC')  #hesh Meas 12$VDC:  11 ;40  ;0.1  ;True ;3.000
VDC(value=12,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 13$VDC')  #hesh Meas 13$VDC:  12 ;40  ;0.1  ;True ;3.000
VDC(value=13,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 14$VDC')  #hesh Meas 14$VDC:  13 ;40  ;0.1  ;True ;3.000
VDC(value=14,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 15$VDC')  #hesh Meas 15$VDC:  14 ;40  ;0.1  ;True ;3.000
VDC(value=15,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 16$VDC')  #hesh Meas 16$VDC:  15 ;40  ;0.1  ;True ;3.000
VDC(value=16,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 17$VDC')  #hesh Meas 17$VDC:  16 ;40  ;0.1  ;True ;3.000
VDC(value=17,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 18$VDC')  #hesh Meas 18$VDC:  17 ;40  ;0.1  ;True ;3.000
VDC(value=18,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 19$VDC')  #hesh Meas 19$VDC:  18 ;40  ;0.1  ;True ;3.000
VDC(value=19,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 20$VDC')  #hesh Meas 20$VDC:  19 ;40  ;0.1  ;True ;3.000
VDC(value=20,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 21$VDC')  #hesh Meas 21$VDC:  20 ;40  ;0.1  ;True ;3.000
VDC(value=21,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3, hesh='Meas 22$VDC')  #hesh Meas 22$VDC:  21 ;40  ;0.1  ;True ;3.000
VDC(value=22,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 23$VDC')  #hesh Meas 23$VDC:  22 ;40  ;0.1  ;False;3.000
VDC(value=23,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 24$VDC')  #hesh Meas 24$VDC:  23 ;40  ;0.1  ;False;3.000
VDC(value=24,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 25$VDC')  #hesh Meas 25$VDC:  24 ;40  ;0.1  ;False;3.000
VDC(value=25,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 26$VDC')  #hesh Meas 26$VDC:  25 ;40  ;0.1  ;False;3.000
VDC(value=26,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 27$VDC')  #hesh Meas 27$VDC:  26 ;40  ;0.1  ;False;3.000
VDC(value=27,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 28$VDC')  #hesh Meas 28$VDC:  27 ;40  ;0.1  ;False;3.000
VDC(value=28,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 29$VDC')  #hesh Meas 29$VDC:  28 ;40  ;0.1  ;False;3.000
VDC(value=29,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 30$VDC')  #hesh Meas 30$VDC:  29 ;40  ;0.1  ;False;3.000
VDC(value=30,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 31$VDC')  #hesh Meas 31$VDC:  30 ;40  ;0.1  ;False;3.000
VDC(value=31,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 32$VDC')  #hesh Meas 32$VDC:  31 ;40  ;0.1  ;False;3.000
VDC(value=32,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 33$VDC')  #hesh Meas 33$VDC:  32 ;40  ;0.1  ;False;3.000
VDC(value=33,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 34$VDC')  #hesh Meas 34$VDC:  33 ;40  ;0.1  ;False;3.000
VDC(value=34,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 35$VDC')  #hesh Meas 35$VDC:  34 ;40  ;0.1  ;False;3.000
VDC(value=35,  range_value=40, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3, hesh='Meas 36$VDC')  #hesh Meas 36$VDC:  35 ;40  ;0.1  ;False;3.000

Testing.GetScreenshot()
Testing.SET_OUTPUT_OFF()
#endregion Voltage measurement$VDC

#region Current measurement$IDC
#description: value \nmeasurement, A;range value, A;allowable\nstabilization\nfactor;is operating\nrange,\nTrue or False;delay time \nbefore \nmeasurement, s;
MOKO.Program('tree', 'set', 'select = Current measurement$IDC')

MOKO.Stage('Set NameGraph => IDC_GRAPH')
Testing.NameGraph = 'IDC_GRAPH'

IDC(value=0.01, range_value=5, allowable_stabilization_factor=0,   is_operating_range=False, time_delay=3,   hesh='Meas 1$IDC')   #hesh Meas 1$IDC:  0.01 ;5  ;0    ;False;3.000
IDC(value=0.1,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 2$IDC')   #hesh Meas 2$IDC:  0.1  ;5  ;0.1  ;False;3.000
IDC(value=0.2,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 3$IDC')   #hesh Meas 3$IDC:  0.2  ;5  ;0.1  ;False;3.000
IDC(value=0.3,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 4$IDC')   #hesh Meas 4$IDC:  0.3  ;5  ;0.1  ;False;3.000
IDC(value=0.4,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 5$IDC')   #hesh Meas 5$IDC:  0.4  ;5  ;0.1  ;False;3.000
IDC(value=0.5,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 6$IDC')   #hesh Meas 6$IDC:  0.5  ;5  ;0.1  ;False;3.000
IDC(value=0.6,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 7$IDC')   #hesh Meas 7$IDC:  0.6  ;5  ;0.1  ;False;3.000
IDC(value=0.7,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 8$IDC')   #hesh Meas 8$IDC:  0.7  ;5  ;0.1  ;False;3.000
IDC(value=0.8,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 9$IDC')   #hesh Meas 9$IDC:  0.8  ;5  ;0.1  ;False;3.000
IDC(value=0.9,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 10$IDC')  #hesh Meas 10$IDC: 0.9  ;5  ;0.1  ;False;3.000
IDC(value=1.0,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 11$IDC')  #hesh Meas 11$IDC: 1.0  ;5  ;0.1  ;True ;3.000
IDC(value=1.1,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 12$IDC')  #hesh Meas 12$IDC: 1.1  ;5  ;0.1  ;True ;3.000
IDC(value=1.2,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 13$IDC')  #hesh Meas 13$IDC: 1.2  ;5  ;0.1  ;True ;3.000
IDC(value=1.3,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 14$IDC')  #hesh Meas 14$IDC: 1.3  ;5  ;0.1  ;True ;3.000
IDC(value=1.4,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 15$IDC')  #hesh Meas 15$IDC: 1.4  ;5  ;0.1  ;True ;3.000
IDC(value=1.5,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 16$IDC')  #hesh Meas 16$IDC: 1.5  ;5  ;0.1  ;True ;3.000
IDC(value=1.6,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 17$IDC')  #hesh Meas 17$IDC: 1.6  ;5  ;0.1  ;True ;3.000
IDC(value=1.7,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 18$IDC')  #hesh Meas 18$IDC: 1.7  ;5  ;0.1  ;True ;3.000
IDC(value=1.8,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 19$IDC')  #hesh Meas 19$IDC: 1.8  ;5  ;0.1  ;True ;3.000
IDC(value=1.9,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 20$IDC')  #hesh Meas 20$IDC: 1.9  ;5  ;0.1  ;True ;3.000
IDC(value=2.0,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 21$IDC')  #hesh Meas 21$IDC: 2.0  ;5  ;0.1  ;True ;3.000
IDC(value=2.1,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=True,  time_delay=3,   hesh='Meas 22$IDC')  #hesh Meas 22$IDC: 2.1  ;5  ;0.1  ;True ;3.000
IDC(value=2.2,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 23$IDC')  #hesh Meas 23$IDC: 2.2  ;5  ;0.1  ;False;3.000
IDC(value=2.3,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 24$IDC')  #hesh Meas 24$IDC: 2.3  ;5  ;0.1  ;False;3.000
IDC(value=2.4,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 25$IDC')  #hesh Meas 25$IDC: 2.4  ;5  ;0.1  ;False;3.000
IDC(value=2.5,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 26$IDC')  #hesh Meas 26$IDC: 2.5  ;5  ;0.1  ;False;3.000
IDC(value=2.6,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 27$IDC')  #hesh Meas 27$IDC: 2.6  ;5  ;0.1  ;False;3.000
IDC(value=2.7,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 28$IDC')  #hesh Meas 28$IDC: 2.7  ;5  ;0.1  ;False;3.000
IDC(value=2.8,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 29$IDC')  #hesh Meas 29$IDC: 2.8  ;5  ;0.1  ;False;3.000
IDC(value=2.9,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 30$IDC')  #hesh Meas 30$IDC: 2.9  ;5  ;0.1  ;False;3.000
IDC(value=3.0,  range_value=5, allowable_stabilization_factor=0.1, is_operating_range=False, time_delay=3,   hesh='Meas 31$IDC')  #hesh Meas 31$IDC: 3.0  ;5  ;0.1  ;False;3.000

Testing.GetScreenshot()
Testing.SET_OUTPUT_OFF()
#endregion Current measurement$IDC

MOKO.Stage(" ")
MOKO.Stage('name: Graph >> mode: close >> command: ', 'Plugin')
MOKO.Plugin("Graph", 'close', '')
MOKO.EndScript()
