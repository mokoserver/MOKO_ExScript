from pressurelib import *
from MOSC import Utility_to_Report

#Region 1.1 Этапы регистрации:
#hesh Заполнение формы
#EndRegion 1.1 Этапы регистрации:


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

MOKO.Stage('Подключение ADT761')
MOKO.Messenger('set', 'Подключение ADT761.png', 'Пожалуйста, подключите ADT761 к испытуемому образцу.')
MOKO.Stage('Проверка формы поверки')
MOKO.Messenger('set', 'Заполнение формы.png', 'Пожалуйста, заполните форму поверки.', '','3')
MOKO.Utility(UN, 'set', 'info')
Utility_to_Report(reports, UN, 'strings')

MOKO.Program('tree', 'set', 'select = ' + 'Заполнение формы')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()
