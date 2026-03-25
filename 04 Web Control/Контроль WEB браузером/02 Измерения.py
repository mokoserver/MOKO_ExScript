import os
import WebActions as wa
from MOKO import Stage, EndScript, Program, Report
from datetime import datetime
import MOSC

StartTime = datetime.now()

try:
    #region Шаг 1: Инициализация и вход$INIT
    Program('tree', 'set', 'select = Шаг 1: Инициализация и вход$INIT')
    Stage("--- Шаг 1: Инициализация и вход ---")
    browser = wa.initialize_browser()
    wa.login_to_router(browser, "admin", "password123")
    #endregion

    #region Шаг 2: Проведение измерений$MEASURE
    #description: ID точки;Уровень мощности;Канал;
    Program('tree', 'set', 'select = Шаг 2: Проведение измерений$MEASURE')
    Stage("--- Шаг 2: Проведение измерений ---")

    Report("Производительность Wi-Fi Пакет 1", 'info', 'table', "ID точки#100;Уровень мощности#100;Канал#100;Мощность передачи#100;Эффективная скорость#100")

    wa.run_test_point_batch1(browser, 'Измерение 1$MEASURE', 1, 'low',    'auto') #hash Измерение 1$MEASURE: 1;low;auto
    wa.run_test_point_batch1(browser, 'Измерение 2$MEASURE', 2, 'low',    1)      #hash Измерение 2$MEASURE: 2;low;1
    wa.run_test_point_batch1(browser, 'Измерение 3$MEASURE', 3, 'medium', 6)      #hash Измерение 3$MEASURE: 3;medium;6
    wa.run_test_point_batch1(browser, 'Измерение 4$MEASURE', 4, 'medium', 11)     #hash Измерение 4$MEASURE: 4;medium;11
    wa.run_test_point_batch1(browser, 'Измерение 5$MEASURE', 5, 'high',   'auto') #hash Измерение 5$MEASURE: 5;high;auto
    wa.run_test_point_batch1(browser, 'Измерение 6$MEASURE', 6, 'high',   1)      #hash Измерение 6$MEASURE: 6;high;1
    wa.run_test_point_batch1(browser, 'Измерение 7$MEASURE', 7, 'high',   6)      #hash Измерение 7$MEASURE: 7;high;6
    wa.run_test_point_batch1(browser, 'Измерение 8$MEASURE', 8, 'high',   11)     #hash Измерение 8$MEASURE: 8;high;11
    wa.run_test_point_batch1(browser, 'Измерение 9$MEASURE', 9, 'medium', 'auto') #hash Измерение 9$MEASURE: 9;medium;auto
    wa.run_test_point_batch1(browser, 'Измерение 10$MEASURE', 10, 'low',  6)      #hash Измерение 10$MEASURE: 10;low;6
    #endregion

    #region Шаг 3: Дополнительные измерения$MEASURE2
    #description: ID точки;Уровень мощности;Канал;
    Program('tree', 'set', 'select = Шаг 3: Дополнительные измерения$MEASURE2')
    Stage("--- Шаг 3: Дополнительные измерения ---")

    Report("Производительность Wi-Fi Дополнительно", 'info', 'table', "ID точки#100;Уровень мощности#100;Канал#100;Мощность передачи#100;Эффективная скорость#100")

    wa.run_test_point_additional(browser, 'Измерение 11$MEASURE2', 11, 'low',    1)   #hash Измерение 11$MEASURE2: 11;low;1
    wa.run_test_point_additional(browser, 'Измерение 12$MEASURE2', 12, 'low',    6)   #hash Измерение 12$MEASURE2: 12;low;6
    wa.run_test_point_additional(browser, 'Измерение 13$MEASURE2', 13, 'low',    11)  #hash Измерение 13$MEASURE2: 13;low;11
    wa.run_test_point_additional(browser, 'Измерение 14$MEASURE2', 14, 'medium', 'auto') #hash Измерение 14$MEASURE2: 14;medium;auto
    wa.run_test_point_additional(browser, 'Измерение 15$MEASURE2', 15, 'medium', 1)   #hash Измерение 15$MEASURE2: 15;medium;1
    wa.run_test_point_additional(browser, 'Измерение 16$MEASURE2', 16, 'medium', 6)   #hash Измерение 16$MEASURE2: 16;medium;6
    wa.run_test_point_additional(browser, 'Измерение 17$MEASURE2', 17, 'high',   'auto') #hash Измерение 17$MEASURE2: 17;high;auto
    wa.run_test_point_additional(browser, 'Измерение 18$MEASURE2', 18, 'high',   1)   #hash Измерение 18$MEASURE2: 18;high;1
    wa.run_test_point_additional(browser, 'Измерение 19$MEASURE2', 19, 'high',   6)   #hash Измерение 19$MEASURE2: 19;high;6
    wa.run_test_point_additional(browser, 'Измерение 20$MEASURE2', 20, 'high',   11)  #hash Измерение 20$MEASURE2: 20;high;11
    #endregion

    Stage("\nСценарий измерений успешно выполнен!", "info")

except Exception as e:
    Stage(f"\nПроизошла критическая ошибка: {e}", "error")

finally:
    if 'browser' in locals() and browser:
        #region Шаг 4: Закрыть браузер$CLOSE1
        Program('tree', 'set', 'select = Шаг 4: Закрыть браузер$CLOSE1')
        Stage("--- Шаг 4: Закрыть браузер ---")
        wa.close_browser(browser)
        #endregion
    MOSC.ScriptExecutionTime(StartTime)
    EndScript()
