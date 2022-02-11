from pressurelib import *

#Region 3.1 Этапы формирования:

#hesh Автосохранение результатов
#hesh Формирование протокола
#EndRegion 3.1 Этапы формирования:

PermissibleError = MOKO.Report('PermissibleError', 'get', 'string', 'string', 'string')  # Пределы допускаемой погрешности
UnitOfMeasure = MOKO.Report('UnitOfMeasure', 'get', 'string', 'string', 'string')  # единицы измерения
MOKO.Report('PermissibleErr;UnitofMeasure;UnitofMeasure1;UnitofMeasure2;UnitofMeasure3;UnitofMeasure4', 'set', 'strings',
            f'{PermissibleError};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};')
MOKO.Report('UoM1;UoM2;UoM3;UoM4', 'set', 'strings', f'{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};')

MOKO.Program('tree', 'set', 'select = ' + 'Автосохранение результатов')
MOKO.Program('tree', 'set', 'chosen = passed')

report = MOKO.Report('ReportPrint', 'get', 'string', 'string', 'string')
report = 'True'
if report == 'True':
    MOKO.Program('Control', 'set', 'Save word report')
MOKO.Program('Control', 'set', 'Save project report')

MOKO.Program('tree', 'set', 'select = ' + 'Формирование протокола')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Stage('Поверка завершена.', 'info')

MOKO.EndScript()
