import MOKO
import MGPH

#Region Status (статус)
#hash Plugin set

MOKO.Messenger('set', 'Plugin - set.png', 'В текущем скрипте будет продемонстрирована команда \'\'set\'\', '
                                          'которая передает данные в плагин. '
                                          'В данном скрипте отрисуется линия в плагине Graph.')


#First Plot
name = "Plot 1"
ArrOy = [300,300]
ArrOx = [0,0.04]
LineWidth = "3"
Color = "FF00FF" #Magenta
Visible = "Yes"
MGPH.AddLine(name, ArrOy, ArrOx, LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'select = ' + 'Plugin set')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()
