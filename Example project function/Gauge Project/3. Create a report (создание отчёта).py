from pressurelib import *

MOKO.Stage('Start script', 'info')
PermissibleError = MOKO.Report('PermissibleError', 'get', 'string', 'string', 'string')  # Пределы допускаемой погрешности
UnitOfMeasure = MOKO.Report('UnitOfMeasure', 'get', 'string', 'string', 'string')  # единицы измерения
MOKO.Report('PermissibleErr;UnitofMeasure;UnitofMeasure1;UnitofMeasure2;UnitofMeasure3;UnitofMeasure4', 'set', 'strings',
            f'{PermissibleError};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};')
MOKO.Report('UoM1;UoM2;UoM3;UoM4', 'set', 'strings', f'{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};{UnitOfMeasure};')

report = MOKO.Report('ReportPrint', 'get', 'string', 'string', 'string')
if report == 'True':
    MOKO.Program('Control', 'set', 'Save word report')
MOKO.Program('Control', 'set', 'Save project report')

MOKO.Stage('Поверка завершена.', 'info')
MOKO.Stage('Finish script', 'info')

MOKO.EndScript()
