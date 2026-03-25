import os
import WebActions as wa
from MOKO import Stage, EndScript, Program, Report
from datetime import datetime
import MOSC

browser = None

StartTime = datetime.now()

try:
    #region Шаг 1: Инициализация и вход (Пакет 3)$INIT3
    Program('tree', 'set', 'select = Шаг 1: Инициализация и вход (Пакет 3)$INIT3')
    Stage("--- Шаг 1: Инициализация и вход (Пакет 3) ---")
    browser = wa.initialize_browser()
    wa.login_to_router(browser, "admin", "password123")
    #endregion

    #region Свернуть браузер (Пакет 3)$MIN3
    Program('tree', 'set', 'select = Свернуть браузер (Пакет 3)$MIN3')
    Stage("--- Свернуть браузер (Пакет 3) ---")
    wa.minimize_browser(browser)
    #endregion

    #region Шаг 2: Проведение измерений (Пакет 3)$MEASURE3
    #description: ID точки;Уровень мощности;Канал;
    Program('tree', 'set', 'select = Шаг 2: Проведение измерений (Пакет 3)$MEASURE3')
    Stage("--- Шаг 2: Проведение измерений (Пакет 3) ---")

    Report("Производительность Wi-Fi Пакет 3", 'info', 'table', "ID точки#100;Уровень мощности#100;Канал#100;Мощность передачи#100;Эффективная скорость#100")

    wa.run_test_point_batch3(browser, 'Измерение 31$MEASURE3', 31, 'low',     'auto') #hash Измерение 31$MEASURE3: 31;low;auto
    wa.run_test_point_batch3(browser, 'Измерение 32$MEASURE3', 32, 'low',     1)      #hash Измерение 32$MEASURE3: 32;low;1
    wa.run_test_point_batch3(browser, 'Измерение 33$MEASURE3', 33, 'medium',  6)      #hash Измерение 33$MEASURE3: 33;medium;6
    wa.run_test_point_batch3(browser, 'Измерение 34$MEASURE3', 34, 'high',    11)     #hash Измерение 34$MEASURE3: 34;high;11
    wa.run_test_point_batch3(browser, 'Измерение 35$MEASURE3', 35, 'high',    'auto') #hash Измерение 35$MEASURE3: 35;high;auto
    #endregion

    Stage("\nСценарий измерений (Пакет 3) успешно выполнен!", "info")

except Exception as e:
    Stage(f"\nПроизошла критическая ошибка: {e}", "error")

finally:
    if 'browser' in locals() and browser:
        #region Шаг 3: Закрыть браузер (Пакет 3)$CLOSE3
        Program('tree', 'set', 'select = Шаг 3: Закрыть браузер (Пакет 3)$CLOSE3')
        Stage("--- Шаг 3: Закрыть браузер (Пакет 3) ---")
        wa.close_browser(browser)
        #endregion
    MOSC.ScriptExecutionTime(StartTime)
    EndScript()
