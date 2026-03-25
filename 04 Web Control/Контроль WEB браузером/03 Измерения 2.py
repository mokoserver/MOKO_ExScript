import os
import time
import WebActions as wa
from MOKO import Stage, EndScript, Program, Report
from datetime import datetime
import MOSC

browser = None

StartTime = datetime.now()

try:
    #region Шаг 1: Инициализация и вход (Пакет 2)$INIT2
    Program('tree', 'set', 'select = Шаг 1: Инициализация и вход (Пакет 2)$INIT2')
    Stage("--- Шаг 1: Инициализация и вход (Пакет 2) ---")
    browser = wa.initialize_browser()
    wa.login_to_router(browser, "admin", "password123")
    #endregion

    #region Скрыть браузер (Пакет 2)$HIDE2
    Program('tree', 'set', 'select = Скрыть браузер (Пакет 2)$HIDE2')
    Stage("--- Скрыть браузер (Пакет 2) ---")
    wa.hide_browser(browser)
    #endregion

    #region Шаг 2: Проведение измерений (Пакет 2)$MEASURE2
    #description: ID точки;Уровень мощности;Канал;
    Program('tree', 'set', 'select = Шаг 2: Проведение измерений (Пакет 2)$MEASURE2')
    Stage("--- Шаг 2: Проведение измерений (Пакет 2) ---")

    Report("Производительность Wi-Fi Пакет 2", 'info', 'table', "ID точки#100;Уровень мощности#100;Канал#100;Мощность передачи#100;Эффективная скорость#100")

    wa.run_test_point_batch2(browser, 'Измерение 21$MEASURE2', 21, 'low',    'auto') #hash Измерение 21$MEASURE2: 21;low;auto
    wa.run_test_point_batch2(browser, 'Измерение 22$MEASURE2', 22, 'low',    1)      #hash Измерение 22$MEASURE2: 22;low;1
    wa.run_test_point_batch2(browser, 'Измерение 23$MEASURE2', 23, 'low',    6)      #hash Измерение 23$MEASURE2: 23;low;6
    wa.run_test_point_batch2(browser, 'Измерение 24$MEASURE2', 24, 'low',    11)     #hash Измерение 24$MEASURE2: 24;low;11
    wa.run_test_point_batch2(browser, 'Измерение 25$MEASURE2', 25, 'medium', 'auto') #hash Измерение 25$MEASURE2: 25;medium;auto
    wa.run_test_point_batch2(browser, 'Измерение 26$MEASURE2', 26, 'medium', 1)      #hash Измерение 26$MEASURE2: 26;medium;1
    wa.run_test_point_batch2(browser, 'Измерение 27$MEASURE2', 27, 'medium', 6)      #hash Измерение 27$MEASURE2: 27;medium;6
    wa.run_test_point_batch2(browser, 'Измерение 28$MEASURE2', 28, 'high',   'auto') #hash Измерение 28$MEASURE2: 28;high;auto
    wa.run_test_point_batch2(browser, 'Измерение 29$MEASURE2', 29, 'high',   1)      #hash Измерение 29$MEASURE2: 29;high;1
    wa.run_test_point_batch2(browser, 'Измерение 30$MEASURE2', 30, 'high',   11)     #hash Измерение 30$MEASURE2: 30;high;11
    #endregion

    Stage("\nСценарий измерений (Пакет 2) успешно выполнен!", "info")

except Exception as e:
    Stage(f"\nПроизошла критическая ошибка: {e}", "error")

finally:
    if 'browser' in locals() and browser:
        #region Шаг 3: Закрыть браузер (Пакет 2)$CLOSE2
        Program('tree', 'set', 'select = Шаг 3: Закрыть браузер (Пакет 2)$CLOSE2')
        Stage("--- Шаг 3: Закрыть браузер (Пакет 2) ---")
        wa.close_browser(browser)
        #endregion
    MOSC.ScriptExecutionTime(StartTime)
    EndScript()
