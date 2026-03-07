
import MOKO

#Region Сбор данных
MOKO.Report(f'test1', 'set',  'string', 'Hello Dolly') #hash Измерение 1
MOKO.Program("tree", "set", "select = Измерение 1")
MOKO.Program('tree', 'set', 'chosen=passed')
MOKO.Report(f'test2', 'set',  'string', 'Hello World') #hash Измерение 2
MOKO.Program("tree", "set", "select = Измерение 2")
MOKO.Program('tree', 'set', 'chosen=passed')
MOKO.Report(f'test3', "info", "table", "Column1#50;" + "Column2#50;" + "Column3#50;" + "Column4#50;") #hash Измерение 3
MOKO.Program("tree", "set", "select = Измерение 3")
MOKO.Report(f'test3', "set",  "table", "T-800;" + "T-1000;" + "TX;" + "T-3000;")

MOKO.Program('tree', 'set', 'chosen=passed')
#EndRegion Сбор данных


#Region Сбор пользовательских значений
#hash Выбор имени протокола
MOKO.Program("tree", "set", "select = Выбор имени протокола")
ReportName = MOKO.Messenger("get", "Имя", "Введите желаемое имя протокола испытаний", "string")

MOKO.Program("control", "set", "UseCustomReportName = true")
MOKO.Program("control", "set", f"UserReportName = {ReportName}")

MOKO.Program('tree', 'set', 'chosen=passed')

#hash Выбор месторасположения протокола
MOKO.Program("tree", "set", "select = Выбор месторасположения протокола")
MOKO.Program("control", "set", "UseCustomPathName = true")
MOKO.Program("control", "set", "UserPathName = C:\MOKO SE\Projects\Tests\WordReport")

MOKO.Program('tree', 'set', 'chosen=passed')
#EndRegion Сбор пользовательских значений

#Region Формирование отчета
#hash Составление протокола
MOKO.Program("tree", "set", "select = Составление протокола")
MOKO.Program('Control', 'set', 'Save project report')
MOKO.Program('Control', 'set', 'Save word report')

MOKO.Program('tree', 'set', 'chosen=passed')
#EndRegion Формирование отчета


MOKO.EndScript('passed')

