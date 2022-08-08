from pressurelib import *

MOKO.Stage('Start script', 'info')
AccuracyClass = float(MOKO.Report('AccuracyClass', 'get', 'string', 'string', 'string').replace(',', '.'))  # класс точности
UnitOfMeasure = MOKO.Report('UnitOfMeasure', 'get', 'string', 'string', 'string')  # единицы измерения
ScaleMax = float(MOKO.Report('ScaleMax', 'get', 'string', 'string', 'string').replace(',', '.'))  # Предельное значение давления на шкале прибора
FirstPoint = float(MOKO.Report('FirstPoint', 'get', 'string', 'string', 'string').replace(',', '.'))  # Первая поверяемая точка на шкале прибора после нуля
PermissibleError = MOKO.Report('PermissibleError', 'get', 'string', 'string', 'string')  # Пределы допускаемой погрешности
Driver = MOKO.Report('Driver', 'get', 'string', 'string', 'string')  # драйвер
MOKO.Report('MeasuringRange', 'set', 'string', '(0-' + str(ScaleMax).replace('.', ',') + ')')
WorkplaceNumber = MOKO.Report('WorkplaceNumber', 'get', 'string', 'string', 'string')  # номер образца
TypeofUnit = MOKO.Report('TypeofUnit', 'get', 'string', 'string', 'string')  # тип образца
ValueofDivision = MOKO.Report('ValueofDivision', 'get', 'string', 'string', 'string')  # цена деления
StampNumber = MOKO.Report('StampNumber', 'get', 'string', 'string', 'string')  # Номер штампа

a = bool(MOKO.Messenger('get', 'Внешний осмотр.jpg', 'Пожалуйста, проведите внешний осмотр образца. Соответствует ли внешний вид образца '
                                                     'установленным нормам?', 'boolean'))
if a:
    appearance = "соответствует"
else:
    appearance = "не соответствует"

Simulation = driver_choice(Driver)  # Driver initialisation
permissible_err = ScaleMax * 0.01 * AccuracyClass
#meas_error = ScaleMax * AccuracyClass / 100
checkpoints = [round(x * FirstPoint, 1) for x in range(int(ScaleMax / FirstPoint) + 1)]  # calculating checkpoints for measurement
checkpoints = final_checkpoints(checkpoints)
if not Simulation:
    set_unit_of_measure(Driver, UnitOfMeasure)  # Setting up units of measure at reference
res_up = from_zero_to_max(checkpoints, Driver, UnitOfMeasure, Simulation)  # Going up from zero to max
# 5 minutes break between the measures
MOKO.Messenger('set', 'Ожидание.jpg', 'Пожалуйста, подождите 5 минут между измерениями.', 'void', '300')

res_down = from_max_to_zero(checkpoints, Driver, UnitOfMeasure, Simulation)  # Going up from zero to max
res_down = list(reversed(res_down))
err_up, err_down, variation = calc_err_variation(checkpoints, res_up, res_down)  # Calculating absolute measurement error and variation
max_err_up, max_err_down = max_err(err_up, err_down)

# Calculation of max and permissible errors
if max_err_up == '-' or max_err_down == '-':
    max_err = '-'
else:
    max_err = max([max_err_up, max_err_down], key=abs)
result, conclusion = conclusion(max_err, permissible_err, appearance)

results(WorkplaceNumber, TypeofUnit, ScaleMax, AccuracyClass, ValueofDivision, appearance, result, StampNumber)
# Reports
reports(checkpoints, res_up, res_down, err_up, err_down, variation, UnitOfMeasure, PermissibleError, max_err)

MOKO.Report('Appearance;Conclusion', 'set', 'strings', f'{appearance};{conclusion}')
MOKO.Report('Res_table1', 'set', 'table', ' ' + ';' + ' ' + ';' + ' ' + ';' + ' ' + ';' + ' ' + ';' + ' ' + ';' + ' ')
MOKO.Stage('Finish script', 'info')

MOKO.EndScript()
