import graph
import MOKO

graph.clear_graph()

name = 'Plot 1'
ArrOx = [0, 1, 2, 3, 4]
ArrOy = [0, 1, 2, 3, 4]
LineWidth = 1
Color = '00FFFF'
Visible = 'Yes'
graph.add_line(name, ArrOy, ArrOx, LineWidth, Color, Visible)
MOKO.Report('Params_Add_Line', 'set', 'string', "name = 'Plot 1'\\narrox = [0, 1, 2, 3, 4]\\narroy = [0, 1, 2, 3, 4]\\n"
                                                "linewidth = 1\\ncolor = '00FFFF'\\nvisible = 'Yes'")
MOKO.Report('Example_Add_Line', 'set', 'string', 'graph.add_line(name, arroy, arrox, linewidth, color, visible)')

graph.write_graph()
MOKO.Report('Write_Graph', 'set', 'string', 'graph.write_graph()')

MOKO.EndScript()




