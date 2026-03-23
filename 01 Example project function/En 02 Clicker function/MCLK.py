'''
Библиотека MCLK.py
===================

Эта библиотека предоставляет высокоуровневый интерфейс для взаимодействия
с плагином "MOKO Clicker" в MOKO SE.

Она инкапсулирует вызовы `MOKO.Plugin("Clicker", ...)` в удобные функции для
автоматизации действий с мышью и работы со скриншотами.
'''
import MOKO

# region ### Initialization / Инициализация ###

# region --- ClickerInit / Инициализация Clicker ---

# -- ClickerInit --
def ClickerInit() -> None:
    """
    Инициализирует плагин MOKO Clicker.

    Этот метод должен быть вызван перед использованием любых других функций
    из этой библиотеки.
    """
    MOKO.Plugin("Clicker", "init", "")
# endregion

# endregion

# region ### Set Commands (Actions) / Команды Установки (Действия) ###

# region --- Mouse Clicks / Клики Мыши ---

# -- MouseLeftClick --
def MouseLeftClick(x: int, y: int) -> None:
    """
    Имитирует клик левой кнопкой мыши по указанным координатам.

    Args:
        x (int): Координата X на экране.
        y (int): Координата Y на экране.
    """
    MOKO.Plugin("Clicker", "set", f"MouseLeftClick = {x} {y}")

# -- MouseRightClick --
def MouseRightClick(x: int, y: int) -> None:
    """
    Имитирует клик правой кнопкой мыши по указанным координатам.

    Args:
        x (int): Координата X на экране.
        y (int): Координата Y на экране.
    """
    MOKO.Plugin("Clicker", "set", f"MouseRightClick = {x} {y}")

# -- MouseMiddleClick --
def MouseMiddleClick(x: int, y: int) -> None:
    """
    Имитирует клик средней кнопкой мыши по указанным координатам.

    Args:
        x (int): Координата X на экране.
        y (int): Координата Y на экране.
    """
    MOKO.Plugin("Clicker", "set", f"MouseMiddleClick = {x} {y}")
# endregion

# region --- Mouse Movement / Перемещение Мыши ---

# -- MouseMove --
def MouseMove(x: int, y: int) -> None:
    """
    Перемещает курсор мыши в указанные координаты.

    Args:
        x (int): Координата X на экране.
        y (int): Координата Y на экране.
    """
    MOKO.Plugin("Clicker", "set", f"MouseMove = {x} {y}")
# endregion

# region --- Screenshots & Files / Скриншоты и Файлы ---

# -- Screenshot --
def Screenshot() -> None:
    """
    Делает скриншот всего экрана.

    Скриншот сохраняется в стандартную директорию плагина:
    "C:/MOKO SE/Plugins/MOKO Clicker/screenshots/"
    """
    MOKO.Plugin("Clicker", "set", "Screenshot")

# -- PngPath --
def PngPath(path: str) -> None:
    """
    Устанавливает путь к PNG-файлу для последующих операций.

    Args:
        path (str): Полный путь к PNG-файлу.
    """
    MOKO.Plugin("Clicker", "set", f"PngPath = {path}")
# endregion

# endregion

# region ### Get Commands (Data Retrieval) / Команды Получения Данных ###

# region --- GetScreenshot / Получить Скриншот ---

# -- GetScreenshot --
def GetScreenshot() -> str:
    """
    Делает скриншот и возвращает его в формате Base64.

    Returns:
        str: Строка с изображением в кодировке Base64.
    """
    screenshot = MOKO.Plugin("Clicker", "get", "Screenshot", "string")
    return screenshot
# endregion

# region --- GetPngFile / Получить PNG Файл ---

# -- GetPngFile --
def GetPngFile() -> str:
    """
    Возвращает содержимое PNG-файла (указанного через PngPath) в формате Base64.

    Returns:
        str: Строка с изображением в кодировке Base64.
    """
    png_file = MOKO.Plugin("Clicker", "get", "PngFile", "string")
    return png_file
# endregion

# region --- GetCoordinates / Получить Координаты ---

# -- GetCoordinates --
def GetCoordinates() -> list:
    """
    Возвращает координаты (x, y), найденные плагином.
    (Предположительно, после поиска изображения на экране)

    Returns:
        list: Список из двух целых чисел [x, y].
    """
    coordinates = MOKO.Plugin("Clicker", "get", "Coordinates", "arrayint")
    return coordinates
# endregion

# endregion
