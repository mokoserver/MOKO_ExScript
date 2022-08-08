from pressurelib import *
from MOSC import Utility_to_Report

MOKO.Stage('Start script', 'info')
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

MOKO.Stage('Проверка формы поверки')
MOKO.Messenger('set', 'Заполнение формы.jpg', 'Пожалуйста, заполните форму поверки.')
MOKO.Utility(UN, 'set', 'info')
Utility_to_Report(reports, UN, 'strings')

# Report print choice:
ReportPrint = MOKO.Messenger('get', 'Открытие отчета.jpg',
                             'Хотите открыть протокол поверки по окончании поверки?', 'boolean')
MOKO.Report('ReportPrint', 'set', 'string', str(ReportPrint))
MOKO.Stage('Finish script', 'info')

MOKO.EndScript()
