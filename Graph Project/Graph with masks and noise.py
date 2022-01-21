import MOKO
import MGPH
import random

def Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2):
    i = 0
    number = 4
    plot_with_masks_n_noise = ''
    while i < len(ArrOx1)/10 and i < 101:
        if i % 50 == 0 and i > 0:
            MOKO.Report(f'Graph_{number}', 'set', 'table', plot_with_masks_n_noise)
            plot_with_masks_n_noise = ''
            number = number + 1

        if i > len(ArrOx) - 1:
            plot_with_masks_n_noise = plot_with_masks_n_noise + f'{i+1};'';'';' \
                                      + f'{i+1};{round(ArrOx1[i],2)};{round(ArrOy1[i],2)};' \
                                      + f'{i+1};'';'';' \
                                      + '\\r'
        else:
            plot_with_masks_n_noise = plot_with_masks_n_noise + f'{i + 1};{round(ArrOx[i], 2)};{round(ArrOy[i], 2)};' \
                                  + f'{i + 1};{round(ArrOx1[i*10], 2)};{round(ArrOy1[i*10], 2)};' \
                                  + f'{i + 1};{round(ArrOx2[i], 2)};{round(ArrOy2[i], 2)};' \
                                  + '\\r'
        i = i + 1

MGPH.ClearGraphCommand()

#High Mask

Value_OyOx = [-160,-50,2.375,2.445]
Name_OyOx = ["Power Spectral Density (dBm/Hz)", "Frequency"]
Autoscale = "No"
MGPH.AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

#Region Status
#description: Width;Color;Visible

name = 'Plot 4' #hesh HighMask:    2;Blue;Yes
MOKO.Report('Name13;Name16;Name19;Name22', 'set', 'strings', f'{name};{name};{name};{name}')
ArrOx = [2.379,2.383,2.4,2.402,2.422,2.424,2.441,2.445]
valueOy = -92
ArrOy = [valueOy,valueOy,valueOy+20,valueOy+40,valueOy+40,valueOy+20,valueOy,valueOy]
LineWidth = 2
Color = '00FFFF' #Blue
Visible = 'Yes'
MGPH.AddLineCommand(name,ArrOy, ArrOx,LineWidth,Color,Visible)

MGPH.WriteGraphCommand()

MOKO.Program('tree', 'set', 'select = ' + 'HighMask')
MOKO.Program('tree', 'set', 'chosen = passed')

#Main Graffic

noise = []
array = []
i = 0
while i < 200:
    noise.append(random.uniform(-136,-118))
    array.append(2.379+(2.39-2.379)/200*i)
    i = i + 1

i = 0
startY = -128
stopY = -108
startX = 2.39
stopX = 2.393
cnt = 75
while i < cnt:
    noise.append(random.uniform(startY,stopY))
    array.append(startX+(stopX-startX)/cnt*i)
    i = i + 1
    if i == cnt and startY == -128:
        i = 0
        startY = -120
        stopY = -102
        startX = 2.393
        stopX = 2.397
    elif i == cnt and startY == -120:
        i = 0
        startY = -112
        stopY = -94
        startX = 2.397
        stopX = 2.401
    elif i == cnt and startY == -112:
        cnt = 25
        i = 0
        startY = -99
        stopY = -86
        startX = 2.401
        stopX = 2.4028

#qweqweq
i = 0
while i < 400:
    noise.append(random.uniform(-80,-56))
    array.append(2.403+(2.422-2.403)/400*i)
    i = i + 1

#afafafaf
i = 0
while i < 10:
    noise.append(random.uniform(-78,-70))
    array.append(2.422+(2.4225-2.422)/10*i)
    i = i + 1

i = 0
while i < 10:
    noise.append(random.uniform(-86,-76))
    array.append(2.4225+(2.423-2.4225)/10*i)
    i = i + 1

i = 0
while i < 10:
    noise.append(random.uniform(-92,-84))
    array.append(2.423+(2.4235-2.423)/10*i)
    i = i + 1

i = 0
while i < 10:
    noise.append(random.uniform(-98,-90))
    array.append(2.4235+(2.424-2.4235)/10*i)
    i = i + 1

i = 0
while i < 10:
    noise.append(random.uniform(-104,-96))
    array.append(2.424+(2.4245-2.424)/10*i)
    i = i + 1

i = 0
while i < 20:
    noise.append(random.uniform(-104,-96))
    array.append(2.4245+(2.4248-2.4245)/20*i)
    i = i + 1

i = 0
while i < 100:
    noise.append(random.uniform(-112,-96))
    array.append(2.4248+(2.43-2.4248)/100*i)
    i = i + 1

i = 0
while i < 100:
    noise.append(random.uniform(-116,-99))
    array.append(2.43+(2.434-2.43)/100*i)
    i = i + 1

i = 0
while i < 200:
    noise.append(random.uniform(-123,-106)) #106
    array.append(2.433+(2.445-2.433)/200*i)
    i = i + 1

name = 'Plot 5' #hesh SignalNoise: 1;Red;Yes
MOKO.Report('Name14;Name17;Name20;Name23', 'set', 'strings', f'{name};{name};{name};{name}')
ArrOx1 = array
ArrOy1 = noise
LineWidth = 1
Color = 'FF0000' #Red
Visible = 'Yes'
MGPH.AddLineCommand(name,ArrOy1, ArrOx1,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'SignalNoise')
MOKO.Program('tree', 'set', 'chosen = passed')

#Low Mask

name = 'Plot 6' #hesh LowMask:  2;Lime;Yes
MOKO.Report('Name15;Name18;Name21;Name24', 'set', 'strings', f'{name};{name};{name};{name}')
ArrOx2 = [2.379,2.383,2.4,2.402,2.422,2.424,2.441,2.445]
valueOy= -150
ArrOy2 = [valueOy,valueOy,valueOy+20,valueOy+40,valueOy+40,valueOy+20,valueOy,valueOy]
LineWidth = 2
Color = '00FF00' #Lime
Visible = 'Yes'
MGPH.AddLineCommand(name,ArrOy2, ArrOx2,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'LowMask')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Status

Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2)

screen = MGPH.GetScreenshotWindow()
MOKO.Report("Screenshot_2_All", 'set', 'picture', screen)
screen = MGPH.GetScreenshotGraph()
MOKO.Report("Screenshot_2_Graph", 'set', 'picture', screen)

#MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()