import MOKO
import time
import numpy as np
import MGPH

MOKO.Report('Graph', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')

def SinusGenerator(x,Ampl,freq,phase):

    sine = Ampl * np.sin(2 * np.pi * freq * x + phase)
    sine = list(sine)
    return sine

def Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2):
    i = 0
    number = 0
    sin_with_diff_phase = ''
    while i < len(ArrOx)+1:
        if i % 50 == 0 and i > 0:
            MOKO.Report(f'Graph_{number}', 'set', 'table', sin_with_diff_phase)
            sin_with_diff_phase = ''
            number = number + 1

        if i < len(ArrOx):
            sin_with_diff_phase = sin_with_diff_phase + f'{i+1};{round(ArrOx[i],2)};{round(ArrOy[i],2)};'\
                                                      + f'{i+1};{round(ArrOx1[i],2)};{round(ArrOy1[i],2)};'\
                                                      + f'{i+1};{round(ArrOx2[i],2)};{round(ArrOy2[i],2)};' \
                                                      + '\\r'
        i = i + 1

MOKO.Plugin('Graph', 'init', '')

time.sleep(4)

MGPH.ClearGraphCommand()

#High Mask

Value_OyOx = [-400,400,0,0.04]
Name_OyOx = ["Amplitude", "Time"]
Autoscale = "No"
MGPH.AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

#4th Plot
name = "Plot 1"
ArrOy = [300,300]
ArrOx = [0,0.04]
LineWidth = 3
Color = "FF00FF" #Magenta
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible)

#5th Plot
name = "Plot 1"
ArrOy = [-300,-300]
ArrOx = [0,0.04]
LineWidth = 3
Color = "FFFF00" #Yellow
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible)

#5th Plot
name = "Plot 1"
ArrOy = [0,0]
ArrOx = [0,0.04]
LineWidth = 3
Color = "0" #Black
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible)

#Region Status
#description: Frequency;Phase;Width;Color;Visible

#First Plot
name = "Plot 1"  #hesh SinusWith Phase90: 40;90;3;Lime;Yes
MOKO.Report('Name1;Name4;Name7;Name10', 'set', 'strings', f'{name};{name};{name};{name}')
sampling_freq = 100
start = 0
stop = 0.05
x = np.arange(start,stop,stop/sampling_freq)
freq = 40
Ampl = 300
ArrOy = SinusGenerator(x,Ampl,freq,90)
ArrOx = list(x)
LineWidth = 3
Color = "00FF00" #Lime
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'SinusWith Phase90')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

# Region Status

#Second Plot
name = "Plot 2" #hesh SinusWithPhase0: 40;0;3;Aqua;Yes
MOKO.Report('Name2;Name5;Name8;Name11', 'set', 'strings', f'{name};{name};{name};{name}')
sampling_freq = 100
start = 0
stop = 0.05
x = np.arange(start,stop,stop/sampling_freq)
freq = 40
Ampl = 300
ArrOy1 = SinusGenerator(x,Ampl,freq,0)
ArrOx1 = list(x)
LineWidth = 3
Color = "00FFFF" #Aqua
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy1, ArrOx1,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'SinusWithPhase0')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

# Region Status

#Third Plot
name = "Plot 3"  #hesh SinusWithPhase-90: 40;-90;3;Red;Yes
MOKO.Report('Name3;Name6;Name9;Name12', 'set', 'strings', f'{name};{name};{name};{name}')
sampling_freq = 100
start = 0
stop = 0.05
x = np.arange(start,stop,stop/sampling_freq)
freq = 40
Ampl = 300
ArrOy2 = SinusGenerator(x,Ampl,freq,-90)
ArrOx2 = list(x)
LineWidth = 3
Color = "FF0000" #Red
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy2, ArrOx2,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'SinusWithPhase-90')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Status

Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2)

screen = MGPH.GetScreenshotWindow()
MOKO.Report("Screenshot_1_All", 'set', 'picture', screen)
screen = MGPH.GetScreenshotGraph()
MOKO.Report("Screenshot_1_Graph", 'set', 'picture', screen)

#MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()