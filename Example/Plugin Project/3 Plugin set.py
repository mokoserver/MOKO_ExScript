import MOKO
import MGPH

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Plugin set


if language == "English":
    MOKO.Messenger('set', 'Plugin - set.png', 'The current script will demonstrate the \'\'set\'\' command, '
                                                 'which passes data to the plugin. This script will draw a line in the Graph plugin.')

elif language == "Русский":
    MOKO.Messenger('set', 'Plugin - set.png', 'В текущем скрипте будет продемонстрирована команда \'\'set\'\', '
                                                 'которая передает данные в плагин. В данном скрипте отрисуется линия в плагине Graph.')


#First Plot
name = "Plot 1"
ArrOy = [300,300]
ArrOx = [0,0.04]
LineWidth = 3
Color = "FF00FF" #Magenta
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'Plugin set')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()