import MOKO
import time
import numpy as np
import MGPH

def SinusGenerator(x,Ampl,freq,phase):

    sine = Ampl * np.sin(2 * np.pi * freq * x + phase)
    sine = list(sine)
    return sine

def Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1):
    i = 0
    number = 8
    sin_with_diff_freq = ''
    while i < 100 + 1:
        if i % 50 == 0 and i > 0:
            MOKO.Report(f'Graph_{number}', 'set', 'table', sin_with_diff_freq)
            sin_with_diff_freq = ''
            number = number + 1

        if i < 100:
            sin_with_diff_freq = sin_with_diff_freq + f'{i + 1};{round(ArrOx[i], 2)};{round(ArrOy[i], 2)};' \
                                                    + f'{i + 1};{round(ArrOx1[i], 2)};{round(ArrOy1[i], 2)};' \
                                                    + '\\r'
        i = i + 1

MGPH.ClearGraphCommand()

Value_OyOx = [-1.1,1.1,-0.01,1]
Name_OyOx = ["Amplitude", "Time"]
Autoscale = "No"
MGPH.AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

#Region Status
#description: Frequency;Phase;Width;Color;Visible

#First Plot
name = "Plot 7" #hesh SinusWithFreq4: 4;0;2;Magenta;Yes
MOKO.Report('Name25;Name27;Name29;Name31', 'set', 'strings', f'{name};{name};{name};{name}')
sampling_freq = 1000
start = 0
stop = 0.5
x = np.arange(start,stop,stop/sampling_freq)
freq = 4
Ampl = 1
ArrOy = SinusGenerator(x,Ampl,freq,0)
ArrOx = list(x)

LineWidth = 2
Color = "FF00FF" #Magenta
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'SinusWithFreq4')
MOKO.Program('tree', 'set', 'chosen = passed')

name = "Plot 8"     #hesh SinusWithFreq30:  30;0;2;DarkTurquoise;Yes
MOKO.Report('Name26;Name28;Name30;Name32', 'set', 'strings', f'{name};{name};{name};{name}')
start = 0
stop = 0.5
x = np.arange(start,stop,stop/sampling_freq)
freq = 30
Ampl = 1
ArrOy1 = SinusGenerator(x,Ampl,freq,0)
start = 0.5
stop = 1.0
x = np.arange(start,stop,stop/sampling_freq)
ArrOx1 = list(x)

LineWidth = 2
Color = "00CED1" #DarkTurquoise
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy1, ArrOx1,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'SinusWithFreq30')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Status

Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1)

screen = MGPH.GetScreenshotWindow()
MOKO.Report("Screenshot_3_All", 'set', 'picture', screen)
screen = MGPH.GetScreenshotGraph()
MOKO.Report("Screenshot_3_Graph", 'set', 'picture', screen)

MOKO.Program('control', 'set', 'save word report')

time.sleep(3)
MGPH.ClearGraphCommand()

MOKO.EndScript()