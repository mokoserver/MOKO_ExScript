from ExFluke5000Agilent34460A import Poverka
import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("************ Measurement Fluke5520 script ***************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Stage('****************** Null flags of system *****************')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

Poverka.LoadTablesHeadInfo()


def VDC(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hesh: str,
        remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()

        Poverka.CheckWireConnection(WireConnection='VDC')
        Poverka.MeasurementStartCommand(WireConnection='VDC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="VDC")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


def VAC(range: (str, float, int), verified: (str, float, int), frequency: (str, float, int), error: (str, float, int),
        filter: (str, float, int), hesh: str, remeasurement: bool = False, remeasurement_number: int = None,
        time_delay: (float, int) = 0):

    if MOSC.HeshStatus(hesh):

        Poverka.CheckConnectDevices()

        Poverka.CheckWireConnection(WireConnection='VAC')
        Poverka.MeasurementStartCommand(WireConnection='VAC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, frequency=frequency, filter=filter,
                                     WireConnection="VAC")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


def R2(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hesh: str,
       remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.HeshStatus(hesh):

        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='R2')
        Poverka.MeasurementStartCommand(WireConnection='R2')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="R2")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


def R4(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hesh: str,
       remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.HeshStatus(hesh):

        Poverka.CheckConnectDevices()
        Poverka.CheckWireConnection(WireConnection='R4')
        Poverka.MeasurementStartCommand(WireConnection='R4')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="R4")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


def IDC(range: (str, float, int), verified: (str, float, int), error: (str, float, int), hesh: str,
        remeasurement: bool = False, remeasurement_number: int = None, time_delay: (float, int) = 0):

    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()

        Poverka.CheckWireConnection(WireConnection='IDC')
        Poverka.MeasurementStartCommand(WireConnection='IDC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, WireConnection="IDC")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


def IAC(range: (str, float, int), verified: (str, float, int), frequency: (str, float, int), error: (str, float, int),
        filter: (str, float, int), hesh: str, remeasurement: bool = False, remeasurement_number: int = None,
        time_delay: (float, int) = 0):

    if MOSC.HeshStatus(hesh):
        Poverka.CheckConnectDevices()

        Poverka.CheckWireConnection(WireConnection='IAC')
        Poverka.MeasurementStartCommand(WireConnection='IAC')

        Poverka.TimeDelay = time_delay
        Poverka.Remeasurement = remeasurement
        Poverka.RemeasurementNumber = remeasurement_number

        Poverka.MeasurementAndReport(range=range, verified=verified, error=error, frequency=frequency, filter=filter,
                                     WireConnection="IAC")

        if Poverka.Status == 'Failed':
            MOSC.hesh_failed()
        else:
            MOSC.hesh_passed()


#region Determining the absolute error of DC voltage measurement$VDC
#description: range of \nmeasurement,\nV;verified point, V;frequency, Hz;filter, Hz;permissible \nmeasurement \nerror, V;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
MOKO.Program('tree', 'set', 'select = Determining the absolute error of DC voltage measurement$VDC')

VDC(range='100m', verified='100,000m',   error='15,5u', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 1$VDC')   #hesh Meas 1$VDC:  100m  ;10,0000m    ;15,5u  ;-  ;-  ;1.000000  ;True  ;3
VDC(range='100m', verified='-100,0000m', error='15,5u', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 2$VDC')   #hesh Meas 2$VDC:  100m  ;-100,0000m  ;15,5u  ;-  ;-  ;1.000000  ;True  ;3
VDC(range='1',    verified='1,000000',   error='90u',   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 3$VDC')   #hesh Meas 3$VDC:  1     ;1,000000    ;90u    ;-  ;-  ;1.000000  ;True  ;3
VDC(range='1',    verified='-1,000000',  error='90u',   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 4$VDC')   #hesh Meas 4$VDC:  1     ;-1,000000   ;90u    ;-  ;-  ;1.000000  ;True  ;3
VDC(range='10',   verified='4,00000',    error='350u',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 5$VDC')   #hesh Meas 5$VDC:  10    ;4,00000     ;350u   ;-  ;-  ;1.000000  ;True  ;3
VDC(range='10',   verified='10,00000',   error='800u',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 6$VDC')   #hesh Meas 6$VDC:  10    ;10,00000    ;800u   ;-  ;-  ;1.000000  ;True  ;3
VDC(range='10',   verified='-10,00000',  error='800u',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 7$VDC')   #hesh Meas 7$VDC:  10    ;-10,00000   ;800u   ;-  ;-  ;1.000000  ;True  ;3
VDC(range='100',  verified='100,0000',   error='9,1m',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 8$VDC')   #hesh Meas 8$VDC:  100   ;100,0000    ;9,1m   ;-  ;-  ;1.000000  ;True  ;3
VDC(range='100',  verified='-100,0000',  error='9,1m',  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 9$VDC')   #hesh Meas 9$VDC:  100   ;-100,0000   ;9,1m   ;-  ;-  ;1.000000  ;True  ;3
VDC(range='1000', verified='1000,000',   error='95m',   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 10$VDC')  #hesh Meas 10$VDC: 1000  ;1000,000    ;95m    ;-  ;-  ;1.000000  ;True  ;3
VDC(range='1000', verified='-500,000',   error='52,5m', time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 11$VDC')  #hesh Meas 11$VDC: 1000  ;-500,000    ;52,5m  ;-  ;-  ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determining the absolute error of DC voltage measurement$VDC

#region Determining the absolute error of AC voltage measurement$VAC
#description: range of \nmeasurement,\nV;verified point, V;frequency, Hz;filter, Hz;permissible \nmeasurement \nerror, V;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements
MOKO.Program('tree', 'set', 'select = Determining the absolute error of AC voltage measurement$VAC')

VAC(range="100m", verified="100,00000m", frequency="1k",    filter="200", error="120u", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 1$VAC')   #hesh Meas 1$VAC:  100m ;100,00000m  ;1k    ;200  ;120u  ;1.000000  ;True  ;3
VAC(range="100m", verified="100,00000m", frequency="50k",   filter="200", error="200u", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 2$VAC')   #hesh Meas 2$VAC:  100m ;100,00000m  ;50k   ;200  ;200u  ;1.000000  ;True  ;3
VAC(range="100m", verified="100,00000m", frequency="300k",  filter="200", error="4,5m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 3$VAC')   #hesh Meas 3$VAC:  100m ;100,00000m  ;300k  ;200  ;4,5m  ;1.000000  ;True  ;3
VAC(range="1",    verified="1,000000",   frequency="1k",    filter="200", error="1,2m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 4$VAC')   #hesh Meas 4$VAC:  1    ;1,000000    ;1k    ;200  ;1,2m  ;1.000000  ;True  ;3
VAC(range="1",    verified="1,000000",   frequency="50k",   filter="200", error="2m",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 5$VAC')   #hesh Meas 5$VAC:  1    ;1,000000    ;50k   ;200  ;2,0m  ;1.000000  ;True  ;3
VAC(range="1",    verified="1,000000",   frequency="300k",  filter="200", error="45m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 6$VAC')   #hesh Meas 6$VAC:  1    ;1,000000    ;300k  ;200  ;45,0m ;1.000000  ;True  ;3
VAC(range="10",   verified="0,03000",    frequency="1k",    filter="200", error="3m",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 7$VAC')   #hesh Meas 7$VAC:  10   ;0,03000     ;1k    ;200  ;3m    ;1.000000  ;True  ;3
VAC(range="10",   verified="1,00000",    frequency="1k",    filter="200", error="3,9m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 8$VAC')   #hesh Meas 8$VAC:  10   ;1,00000     ;1k    ;200  ;3,9m  ;1.000000  ;True  ;3
VAC(range="10",   verified="10,00000",   frequency="0.01k", filter="3",   error="12m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 9$VAC')   #hesh Meas 9$VAC:  10   ;10,00000    ;0,01k ;3    ;12m   ;1.000000  ;True  ;3
VAC(range="10",   verified="10,00000",   frequency="20k",   filter="20",  error="12m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 10$VAC')  #hesh Meas 10$VAC: 10   ;10,00000    ;0,1k  ;20   ;12m   ;1.000000  ;True  ;3
VAC(range="10",   verified="10,00000",   frequency="20k",   filter="200", error="12m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 11$VAC')  #hesh Meas 11$VAC: 10   ;10,00000    ;20k   ;200  ;12m   ;1.000000  ;True  ;3
VAC(range="10",   verified="10,00000",   frequency="50k",   filter="200", error="20m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 12$VAC')  #hesh Meas 12$VAC: 10   ;10,00000    ;50k   ;200  ;20m   ;1.000000  ;True  ;3
VAC(range="10",   verified="10,00000",   frequency="100k",  filter="200", error="71m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 13$VAC')  #hesh Meas 13$VAC: 10   ;10,00000    ;100k  ;200  ;71m   ;1.000000  ;True  ;3
VAC(range="100",  verified="100,0000",   frequency="1k",    filter="200", error="120m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 14$VAC')  #hesh Meas 14$VAC: 100  ;100,0000    ;1k    ;200  ;120m  ;1.000000  ;True  ;3
VAC(range="100",  verified="100,0000",   frequency="50k",   filter="200", error="200m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 15$VAC')  #hesh Meas 15$VAC: 100  ;100,0000    ;50k   ;200  ;200m  ;1.000000  ;True  ;3
VAC(range="750",  verified="750,000",    frequency="1k",    filter="200", error="900m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 16$VAC')  #hesh Meas 16$VAC: 750  ;750,000     ;1k    ;200  ;900m  ;1.000000  ;True  ;3
VAC(range="750",  verified="210,000",    frequency="50k",   filter="200", error="690m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 17$VAC')  #hesh Meas 17$VAC: 750  ;210,000     ;50k   ;200  ;690m  ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determining the absolute error of AC voltage measurement$VAC

#region Determination of the measurement error of the resistance of a 2-wire circuit$R2
#description: range of \nmeasurement,\nOm;verified \npoint, Om;frequency, Hz;filter, Hz;permissible \nmeasurement \nerror, Om;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
MOKO.Program('tree', 'set', 'select = Determination of the measurement error of the resistance of a 2-wire circuit$R2')

R2(range="1M",   verified="1,000000M",  error="150",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 1$R2')  #hesh Meas 1$R2:  1M     ;1,000000M  ;150   ;-  ;-  ;1.000000  ;True  ;3
R2(range="10M",  verified="10,00000M",  error="4,1k", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 2$R2')  #hesh Meas 2$R2:  10M    ;10,00000M  ;4,1k  ;-  ;-  ;1.000000  ;True  ;3
R2(range="100M", verified="100,0000M",  error="810k", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 3$R2')  #hesh Meas 3$R2:  100M   ;100,0000M  ;810k  ;-  ;-  ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determination of the measurement error of the resistance of a 2-wire circuit$R2

#region Determination of the measurement error of the resistance of a 4-wire circuit$R4
#description: range of \nmeasurement,\nOm;verified \npoint, Om;frequency, Hz;filter, Hz;permissible \nmeasurement \nerror, Om;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
MOKO.Program('tree', 'set', 'select = Determination of the measurement error of the resistance of a 4-wire circuit$R4')

R4(range="100",  verified="100,0000",  error="21m",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 1$R4')  #hesh Meas 1$R4:  100    ;100,0000   ;21m   ;-  ;-  ;1.000000  ;True  ;3
R4(range="1k",   verified="1,000000k", error="4,15m", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 2$R4')  #hesh Meas 2$R4:  1k     ;1,000000k  ;4,15m ;-  ;-  ;1.000000  ;True  ;3
R4(range="10k",  verified="10,00000k", error="1,5",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 3$R4')  #hesh Meas 3$R4:  10k    ;10,00000k  ;1,5   ;-  ;-  ;1.000000  ;True  ;3
R4(range="100k", verified="100,0000k", error="15",    time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 4$R4')  #hesh Meas 4$R4:  100k   ;100,0000k  ;15    ;-  ;-  ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determination of the measurement error of the resistance of a 4-wire circuit$R4

#region Determination of the absolute error in the measurement of direct current$IDC
#description: range of \nmeasurement,\nA;verified point, A;frequency, Hz;filter, Hz;permissible \nmeasurement \nerror, A;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
MOKO.Program('tree', 'set', 'select = Determination of the absolute error in the measurement of direct current$IDC')

IDC(range="100u",  verified="10,0000u",  error="0,0750u", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 1$IDC')  #hesh Meas 1$IDC: 100u   ;10,0000u   ;0,0750u ;-  ;-  ;1.000000  ;True  ;3
IDC(range="1m",    verified="1,000000m", error="0,560u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 2$IDC')  #hesh Meas 2$IDC: 1m     ;1,000000m  ;0,560u  ;-  ;-  ;1.000000  ;True  ;3
IDC(range="10m",   verified="10,00000m", error="0,7u",    time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 3$IDC')  #hesh Meas 3$IDC: 10m    ;10,00000m  ;7u      ;-  ;-  ;1.000000  ;True  ;3
IDC(range="100m",  verified="100,0000m", error="0,55u",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 4$IDC')  #hesh Meas 4$IDC: 100m   ;100,0000m  ;55u     ;-  ;-  ;1.000000  ;True  ;3
IDC(range="1",     verified="1,000000",  error="1,1m",    time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 5$IDC')  #hesh Meas 5$IDC: 1      ;1,000000   ;1,1m    ;-  ;-  ;1.000000  ;True  ;3
IDC(range="3",     verified="2,00000",   error="4,6m",    time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 6$IDC')  #hesh Meas 6$IDC: 3      ;2,00000    ;4,6m    ;-  ;-  ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determination of the absolute error in the measurement of direct current$IDC

#region Determination of the absolute error of measuring the strength of alternating current$IAC
#description: range of \nmeasurement,\nA;verified point, A;frequency, Hz;filter, Hz;permissible \nmeasurement \nerror, A;delay time \nbefore \nmeasurement, s;remeasure,\nTrue or False;number of \nremeasurements;
MOKO.Program('tree', 'set', 'select = Determination of the absolute error of measuring the strength of alternating current$IAC')

IAC(range="100u",  verified="100,0000u",  frequency="1k",    filter="200", error="0,14u", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 1$IAC')   #hesh Meas 1$IAC:  100u  ;100,0000u  ;1k     ;200   ;0,14u ;1.000000  ;True  ;3
IAC(range="100u",  verified="100,0000u",  frequency="5k",    filter="200", error="0,14u", time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 2$IAC')   #hesh Meas 2$IAC:  100u  ;100,0000u  ;5k     ;200   ;0,14u ;1.000000  ;True  ;3
IAC(range="1m",    verified="1,000000m",  frequency="1k",    filter="200", error="1,4u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 3$IAC')   #hesh Meas 3$IAC:  1m    ;1,000000m  ;1k     ;200   ;1,4u  ;1.000000  ;True  ;3
IAC(range="1m",    verified="1,000000m",  frequency="5k",    filter="200", error="1,4u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 4$IAC')   #hesh Meas 4$IAC:  1m    ;1,000000m  ;5k     ;200   ;1,4u  ;1.000000  ;True  ;3
IAC(range="10m",   verified="1,00000m",   frequency="1k",    filter="200", error="4,1u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 5$IAC')   #hesh Meas 5$IAC:  10m   ;1,00000m   ;1k     ;200   ;4,1u  ;1.000000  ;True  ;3
IAC(range="10m",   verified="1,00000m",   frequency="1k",    filter="200", error="5,0u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 6$IAC')   #hesh Meas 6$IAC:  10m   ;1,00000m   ;1k     ;200   ;5,0u  ;1.000000  ;True  ;3
IAC(range="10m",   verified="10,00000m",  frequency="1k",    filter="200", error="14u",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 7$IAC')   #hesh Meas 7$IAC:  10m   ;10,00000   ;1k     ;200   ;14u   ;1.000000  ;True  ;3
IAC(range="10m",   verified="10,00000m",  frequency="5k",    filter="200", error="14u",   time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 8$IAC')   #hesh Meas 8$IAC:  10m   ;10,00000   ;5k     ;200   ;14u   ;1.000000  ;True  ;3
IAC(range="100m",  verified="100,0000m",  frequency="0,01k", filter="3",   error="140u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 9$IAC')   #hesh Meas 9$IAC:  100m  ;100,0000   ;0,01k  ;30    ;140u  ;1.000000  ;True  ;3
IAC(range="100m",  verified="100,0000m",  frequency="1k",    filter="200", error="140u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 10$IAC')  #hesh Meas 10$IAC: 100m  ;100,0000   ;1k     ;200   ;140u  ;1.000000  ;True  ;3
IAC(range="100m",  verified="100,0000m",  frequency="5k",    filter="200", error="140u",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 11$IAC')  #hesh Meas 11$IAC: 100m  ;100,0000   ;5k     ;200   ;140u  ;1.000000  ;True  ;3
IAC(range="1",     verified="1,000000",   frequency="1k",    filter="200", error="1,4m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 12$IAC')  #hesh Meas 12$IAC: 1     ;1,000000   ;1k     ;200   ;1,4m  ;1.000000  ;True  ;3
IAC(range="1",     verified="1,000000",   frequency="5k",    filter="200", error="1,4m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 13$IAC')  #hesh Meas 13$IAC: 1     ;1,000000   ;5k     ;200   ;1,4m  ;1.000000  ;True  ;3
IAC(range="3",     verified="2,00000",    frequency="1k",    filter="200", error="5,8m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 14$IAC')  #hesh Meas 14$IAC: 3     ;2,00000    ;1k     ;200   ;5,8m  ;1.000000  ;True  ;3
IAC(range="3",     verified="2,00000",    frequency="5k",    filter="200", error="5,8m",  time_delay=1.0000, remeasurement=True, remeasurement_number=3, hesh='Meas 15$IAC')  #hesh Meas 15$IAC: 3     ;2,00000    ;5k     ;200   ;5,8m  ;1.000000  ;True  ;3

Poverka.MeasurementStopCommand()
#endregion Determination of the absolute error of measuring the strength of alternating current$IAC

MOKO.EndScript()
