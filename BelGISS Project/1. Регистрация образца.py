from pressurelib import *
from MOSC import Utility_to_Report

UN = 'PressureGauge'  # Utility Name
reports = ['AccuracyClass',  # класс точности
           'UnitOfMeasure',  # единицы измерения
           'ScaleMax',  # Предельное значение давления на шкале прибора
           'FirstPoint',  # Первая поверяемая точка на шкале прибора после нуля
           'FirstMultiplePoint',  # Первая кратная пределу поверяемая точка на шкале
           'ValueofDivision',  # цена деления
           'TypeofUnit',  # Тип образца
           'PermissibleError',  # Пределы допускаемой погрешности
           'StampNumber',  # Номер штампа
           'Owner',  # Владелец
           'Verifier',  # ФИО поверителя
           'VerificationLocation',  # Место проведения поверки
           'WorkplaceNumber',  # Номер рабочего места
           'OrderNumber',  # Номер заказа
           'Day',       ###########
           'Month',     ####ДАТА###
           'Year',      ###########
           'ProtocolNumber',  # Номер протокола
           'Temperature',  # Температура
           'Humidity',  # Влажность
           'AmbientPressure',  # Давление окружающей среды
           'Driver',  # Драйвер
           'UnitNumber'  # Номер образца
           ]

MOKO.Stage('Проверка форма поверки')
MOKO.Messenger('set', 'Поверка', 'Пожалуйста, заполните форму поверки.')
MOKO.Utility(UN, 'set', 'info')
Utility_to_Report(reports, UN, 'strings')

# Report print choice:
ReportPrint = MOKO.Messenger('get', 'Протокол поверки',
                             'Хотите открыть протокол поверки по окончании поверки?', 'boolean')
MOKO.Report('ReportPrint', 'set', 'string', str(ReportPrint))

MOKO.EndScript()
