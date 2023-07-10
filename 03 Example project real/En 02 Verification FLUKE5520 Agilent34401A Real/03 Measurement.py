from ExFluke5000Agilent34401A import ExFluke5000Agilent34401A
import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("****************** Measurement script *******************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Stage('**************** Null flags of system ****************')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

Poverka = ExFluke5000Agilent34401A()
Poverka.LoadTablesHeadInfo()


def VDC(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hesh: str):
    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='VDC')
        Poverka.MeasurementStartCommand(WireConnection='VDC')
        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="VDC")

    if Poverka.Status == 'Failed':
        MOSC.hesh_failed()
    else:
        MOSC.hesh_passed()


def VAC(range: (str, float, int), verified: (str, float, int), frequency: (str, float, int), error: (str, float, int),
        hesh: str):
    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='VAC')
        Poverka.MeasurementStartCommand(WireConnection='VAC')
        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, frequency=frequency,
                                     WireConnection="VAC")

    if Poverka.Status == 'Failed':
        MOSC.hesh_failed()
    else:
        MOSC.hesh_passed()


def R2(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hesh: str):
    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='R2')
        Poverka.MeasurementStartCommand(WireConnection='R2')
        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="R2")

    if Poverka.Status == 'Failed':
        MOSC.hesh_failed()
    else:
        MOSC.hesh_passed()


def R4(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hesh: str):
    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='R4')
        Poverka.MeasurementStartCommand(WireConnection='R4')
        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="R4")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


def IDC(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hesh: str):
    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='IDC')
        Poverka.MeasurementStartCommand(WireConnection='IDC')
        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="IDC")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


def IAC(range: (str, float, int), verified: (str, float, int), frequency: (str, float, int), error: (str, float, int),
        hesh: str):
    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='IAC')
        Poverka.MeasurementStartCommand(WireConnection='IAC')
        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, frequency=frequency,
                                     WireConnection="IAC")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


#region Determining the absolute error of AC voltage measurement$VAC
#description: range of \nmeasurement, V;verified point, V;frequency, Hz;range of \npermissible \nabsolute error, V;
MOKO.Program('tree', 'set', 'select = Determining the absolute error of AC voltage measurement$VAC')

VAC(range="100m", verified="100,0000m", frequency="1k",    error="46mk",  hesh='Meas 1$VAC')   #hesh Meas 1$VAC:   100m  ;100,0000m  ;1k    ;46mk;
VAC(range="100m", verified="100,0000m", frequency="1k",    error="100mk", hesh='Meas 2$VAC')   #hesh Meas 2$VAC:   100m  ;100,0000m  ;1k    ;100mk;
VAC(range="100m", verified="100,0000m", frequency="50k",   error="170mk", hesh='Meas 3$VAC')   #hesh Meas 3$VAC:   100m  ;100,0000m  ;50k   ;170mk;
VAC(range="1",    verified="1,000000",  frequency="1k",    error="900mk", hesh='Meas 4$VAC')   #hesh Meas 4$VAC:   1     ;1,000000   ;1k    ;900mk;
VAC(range="1",    verified="1,000000",  frequency="50k",   error="1,7m",  hesh='Meas 5$VAC')   #hesh Meas 5$VAC:   1     ;1,000000   ;50k   ;1,7m;
VAC(range="10",   verified="10,00000",  frequency="0,01k", error="9m",    hesh='Meas 6$VAC')   #hesh Meas 6$VAC:   10    ;10,00000   ;0,01k ;9m;
VAC(range="10",   verified="10,00000",  frequency="1k",    error="9m",    hesh='Meas 7$VAC')   #hesh Meas 7$VAC:   10    ;10,00000   ;1k    ;9m;
VAC(range="10",   verified="10,00000",  frequency="50k",   error="17m",   hesh='Meas 8$VAC')   #hesh Meas 8$VAC:   10    ;10,00000   ;50k   ;17m;
VAC(range="100",  verified="100,0000",  frequency="1k",    error="90m",   hesh='Meas 9$VAC')   #hesh Meas 9$VAC:   100   ;100,0000   ;1k    ;90m;
VAC(range="100",  verified="100,0000",  frequency="50k",   error="170m",  hesh='Meas 10$VAC')  #hesh Meas 10$VAC:  100   ;100,0000   ;50k   ;170m;
VAC(range="750",  verified="750,000",   frequency="1k",    error="675m",  hesh='Meas 11$VAC')  #hesh Meas 11$VAC:  750   ;750,000    ;1k    ;675m;
VAC(range="750",  verified="750,000",   frequency="5k",    error="1275m", hesh='Meas 12$VAC')  #hesh Meas 12$VAC:  750   ;750,000    ;5k    ;1275m;

Poverka.MeasurementStopCommand()
#endregion Determining the absolute error of AC voltage measurement$VAC

#region Determining the absolute error of DC voltage measurement$VDC
#description: range of \nmeasurement, V;verified point, V;range of \npermissible \nabsolute error, V;
MOKO.Program('tree', 'set', 'select = Determining the absolute error of DC voltage measurement$VDC')

VDC(range='100m', verified='100,0000m',  error='8,5mk',  hesh='Meas 1$VDC')   #hesh Meas 1$VDC:  100m   ;100,0000m   ;8,5mk;
VDC(range='100m', verified='-100,0000m', error='8,5mk',  hesh='Meas 2$VDC')   #hesh Meas 2$VDC:  100m   ;-100,0000m  ;8,5mk;
VDC(range='1',    verified='1,000000',   error='47mk',   hesh='Meas 3$VDC')   #hesh Meas 3$VDC:  1      ;1,000000    ;47mk;
VDC(range='1',    verified='-1,000000',  error='47mk',   hesh='Meas 4$VDC')   #hesh Meas 4$VDC:  1      ;-1,000000   ;47mk;
VDC(range='10',   verified='10,00000',   error='400mk',  hesh='Meas 5$VDC')   #hesh Meas 5$VDC:  10     ;10,00000    ;400mk;
VDC(range='10',   verified='-10,00000',  error='400mk',  hesh='Meas 6$VDC')   #hesh Meas 6$VDC:  10     ;-10,00000   ;400mk;
VDC(range='100',  verified='100,0000',   error='5,1m',   hesh='Meas 7$VDC')   #hesh Meas 7$VDC:  100    ;100,0000    ;5,1m;
VDC(range='100',  verified='-100,0000',  error='5,1m',   hesh='Meas 8$VDC')   #hesh Meas 8$VDC:  100    ;-100,0000   ;5,1m;
VDC(range='1000', verified='1000,000',   error='55m',    hesh='Meas 9$VDC')   #hesh Meas 9$VDC:  1000   ;1000,000    ;55m;
VDC(range='1000', verified='-1000,000',  error='55m',    hesh='Meas 10$VDC')  #hesh Meas 10$VDC: 1000   ;-1000,000   ;55m;

Poverka.MeasurementStopCommand()
#endregion Determining the absolute error of DC voltage measurement$VDC

#region Determination of the measurement error of the resistance of a 4-wire circuit$R4
#description: range of \nmeas., Om;verified \npoint, Om;range of \npermissible \nabsl. error, Om;
MOKO.Program('tree', 'set', 'select = Determination of the measurement error of the resistance of a 4-wire circuit$R4')

R4(range="100",  verified="100,000",   error="14m",   hesh='Meas 1$R4')  #hesh Meas 1$R4:  100    ;100,000   ;14m;
R4(range="1k",   verified="1,00000k",  error="110m",  hesh='Meas 2$R4')  #hesh Meas 2$R4:  1k     ;1,00000K  ;110m;
R4(range="10k",  verified="10,0000k",  error="1,1",   hesh='Meas 3$R4')  #hesh Meas 3$R4:  10k    ;10,0000K  ;1,1;
R4(range="100k", verified="100,000k",  error="11",    hesh='Meas 4$R4')  #hesh Meas 4$R4:  100k   ;100,000K  ;11;

Poverka.MeasurementStopCommand()
#endregion Determination of the measurement error of the resistance of a 4-wire circuit$R4

#region Determination of the measurement error of the resistance of a 2-wire circuit$R2
#description: range of \nmeas., Om;verified \npoint, Om;range of \npermissible \nabsl. error, Om;
MOKO.Program('tree', 'set', 'select = Determination of the measurement error of the resistance of a 2-wire circuit$R2')

R2(range="1M",    verified="1,00000M", error="110",  hesh='Meas 1$R2')  #hesh Meas 1$R2:  1M     ;1,00000M  ;110;
R2(range="10M",   verified="10,0000M", error="4,1k", hesh='Meas 2$R2')  #hesh Meas 2$R2:  10M    ;10,0000M  ;4,1k;
R2(range="100M",  verified="100,000M", error="810k", hesh='Meas 3$R2')  #hesh Meas 3$R2:  100M   ;100,000M  ;810k;

Poverka.MeasurementStopCommand()
#endregion Determination of the measurement error of the resistance of a 2-wire circuit$R2

#region Determination of the absolute error of measuring the strength of alternating current$IAC
#description: range of \nmeasurement, A;verified point, A;frequency, Hz;range of \npermissible \nabsolute error, A;
MOKO.Program('tree', 'set', 'select = Determination of the absolute error of measuring the strength of alternating current$IAC')

IAC(range="1", verified="1,00000", frequency="1k",  error="1,4m",   hesh='Meas 1$IAC')  #hesh Meas 1$IAC: 1 ;1,00000   ;1k  ;1,4m;
IAC(range="3", verified="0,30000", frequency="1k",  error="4,8m",   hesh='Meas 2$IAC')  #hesh Meas 2$IAC: 3 ;0,30000   ;1k  ;4,8m;

Poverka.MeasurementStopCommand()
#endregion Determination of the absolute error of measuring the strength of alternating current$IAC


#region Determination of the absolute error in the measurement of direct current$IDC
#description: range of \nmeasurement, A;verified point, A;range of \npermissible \nabsolute error, A;
MOKO.Program('tree', 'set', 'select = Determination of the absolute error in the measurement of direct current$IDC')

IDC(range="10m",   verified="10,00000m",  error="7mk",    hesh='Meas 1$IDC')  #hesh Meas 1$IDC: 10m    ;10,00000m   ;7mk;
IDC(range="100m",  verified="100,0000m",  error="55mk",   hesh='Meas 2$IDC')  #hesh Meas 2$IDC: 100m   ;100,0000m   ;55mk;
IDC(range="1",     verified="1,00000",    error="1,1m",   hesh='Meas 3$IDC')  #hesh Meas 3$IDC: 1      ;1,00000     ;1,1m;
IDC(range="3",     verified="2,00000",    error="3,0m",   hesh='Meas 4$IDC')  #hesh Meas 4$IDC: 3      ;2,00000     ;3,0m;

Poverka.MeasurementStopCommand()
#endregion Determination of the absolute error in the measurement of direct current$IDC

MOKO.EndScript()
