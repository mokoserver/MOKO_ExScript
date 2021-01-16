import MokoRequestLib as Moko
from MokoFormatedLibrary import stars, choice_language
import random


Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

language = choice_language()


if language == 'Russian':
    Moko.Messenger('set', 'Script message',
                   'В текущем скрипте в тестовом протоколе данные записываются в таблицу по определенным закладкам.')
    Moko.Messenger('set', 'Report mode', 'Для создания шапки таблицы функция Report использует тип *info*')

    Moko.Report("table1", 'info', 'table', 'Параметр_1\\nсамый\\nточный #70;Параметр_2#120;Параметр_3;Параметр_4')
    Moko.Report("table2", 'info', 'table', 'Параметр_5;Параметр_6;Параметр_7;Параметр_8')

    while True:
        try:
            num_row = int(Moko.Messenger('get', 'Таблица №1', 'Введите число строк в таблице №1', 'string'))
            break
        except ValueError:
            Moko.Messenger('set', 'Ошибка!', 'Вы не ввели количество строк в таблице №1! Попробуйте ещё раз')

    for x in range(num_row):
        numbers_1 = ''
        for y in range(4):
            number = str(random.uniform(0, 100))
            numbers_1 += 'число:\\n' + number + ','
        Moko.Report("table1", 'set', 'table', numbers_1)

    while True:
        try:
            num_row = int(Moko.Messenger('get', 'Таблица №2', 'Введите число строк в таблице №2', 'string'))
            break
        except ValueError:
            Moko.Messenger('set', 'Ошибка!', 'Вы не ввели количество строк в таблице №2! Попробуйте ещё раз')

    for x in range(num_row):
        numbers_2 = ''
        for y in range(4):
            number = str(random.uniform(0, 100))
            numbers_2 += 'число:\\n' + number + ','
        Moko.Report("table2", 'set', 'table', numbers_2)

elif language == 'English (default)':
    Moko.Messenger('set', 'Script message',
                   'In the current script in the test protocol, data is written to the table according to certain tabs.')
    Moko.Messenger('set', 'Report mode', 'The Report function uses the *info* type to create the table header.')
    Moko.Report("table1", 'info', 'table', 'Param_1;Param_2;Param_3;Param_4')
    Moko.Report("table2", 'info', 'table', 'Param_5;Param_6;Param_7;Param_8')

    while True:
        try:
            num_row = int(Moko.Messenger('get', 'Table №1', 'Enter the number of strings in table №1', 'string'))
            break
        except ValueError:
            Moko.Messenger('set', 'Error!', 'You have not entered the number of rows in table №1! Please try again.')

    for x in range(num_row):
        numbers_1 = ''
        for y in range(4):
            number = str(random.uniform(0, 100))
            numbers_1 += 'number:\\n' + number + ','
        Moko.Report("table1", 'set', 'table', numbers_1)

    while True:
        try:
            num_strings2 = int(Moko.Messenger('get', 'Table №2', 'Enter the number of strings in table №2', 'string'))
            break
        except ValueError:
            Moko.Messenger('set', 'Error!', 'You have mot entered the number of rows in table №2! Please try again.')

    for x in range(num_row):
        numbers_2 = ''
        for y in range(4):
            number = str(random.uniform(0, 100))
            numbers_2 += 'number:\\n' + number + ','
        Moko.Report("table2", 'set', 'table', numbers_2)


Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))
Moko.EndScript()
