import MOKO
from subprocess import Popen, PIPE


###########################################################################################

    ################       ####        ##      ################      ##################
           ##              ## ##       ##             ##                     ##
           ##              ##  ##      ##             ##                     ##
           ##              ##   ##     ##             ##                     ##
           ##              ##    ##    ##             ##                     ##
           ##              ##     ##   ##             ##                     ##
           ##              ##      ##  ##             ##                     ##
           ##              ##       ## ##             ##                     ##
    ################       ##        ####      ################              ##

###########################################################################################


def ClickerInit() -> None:
    """
        This function initializes plugin MOKO Clicker

        :return: None

        >>> ClickerInit()
    """
    MOKO.Plugin("Clicker", "init", "")

    processes = Popen('tasklist', stdin=PIPE, stderr=PIPE, stdout=PIPE).communicate()[0]
    while processes.find("MOKO Clicker".encode("utf8")) == -1:
        MOKO.Stage("Waiting for the plugin to run...")
        processes = Popen('tasklist', stdin=PIPE, stderr=PIPE, stdout=PIPE).communicate()[0]
    return None


###########################################################################################

     #########      ###########      ##################
    ##              ##                       ##
    ##              ##                       ##
    ##              ##                       ##
     ########       #########                ##
            ##      ##                       ##
            ##      ##                       ##
            ##      ##                       ##
    #########       ###########              ##

###########################################################################################


def MouseLeftClickCommand(x:int, y:int) -> None:
    """
        This function imitates pressing mouse left button

        :param x: axis Ox value
        :param y: axis Oy value

        :return: None

        >>> MouseLeftClickCommand(1000, 2000)
        >>> MouseLeftClickCommand("1000", "2000")
    """
    MOKO.Plugin("Clicker", "set", f"MouseLeftClick = {x} {y}")
    return None

def MouseRightClickCommand(x:int, y:int) -> None:
    """
        This function imitates pressing mouse right button

        :param x: axis Ox value
        :param y: axis Oy value

        :return: None

        >>> MouseRightClickCommand(1000, 2000)
        >>> MouseRightClickCommand("1000", "2000")
    """
    MOKO.Plugin("Clicker", "set", f"MouseRightClick = {x} {y}")
    return None

def MouseMiddleClickCommand(x:int, y:int) -> None:
    """
        This function imitates pressing mouse middle button

        :param x: axis Ox value
        :param y: axis Oy value

        :return: None

        >>> MouseMiddleClickCommand(1000, 2000)
        >>> MouseMiddleClickCommand("1000", "2000")
    """
    MOKO.Plugin("Clicker", "set", f"MouseMiddleClick = {x} {y}")
    return None

def MouseMoveCommand(x:int, y:int) -> None:
    """
        This function moves mouse cursor to the point (x,y)

        :param x: axis Ox value
        :param y: axis Oy value

        :return: None

        >>> MouseMoveCommand(1000, 2000)
        >>> MouseMoveCommand("1000", "2000")
    """
    MOKO.Plugin("Clicker", "set", f"MouseMove = {x} {y}")
    return None

def ScreenshotCommand() -> None:
    """
        This function makes a screenshot. The screenshot is saved in "C:/MOKO SE/Plugins/MOKO Clicker/screenshots/"

        :return: None

        >>> ScreenshotCommand()
    """
    MOKO.Plugin("Clicker", "set", f"Screenshot")
    return None

def PngPathCommand(path:str) -> None:
    """
        This function sets a path to the png file.

        :return: None

        >>> PngPathCommand("C:/MOKO SE/Plugins/MOKO Clicker/screenshots/Clicker.png")
    """
    MOKO.Plugin("Clicker", "set", f"PngPath = {path}")
    return None


###########################################################################################

     #########      ###########      ##################
    ##              ##                       ##
    ##              ##                       ##
    ##              ##                       ##
    ##    #####     #########                ##
    ##    #  ##     ##                       ##
    ##       ##     ##                       ##
    ##       ##     ##                       ##
     #########      ###########              ##

###########################################################################################

def GetScreenshotCommand() -> str:
    """
        This function makes a screenshot and returns it in base64 format

        :return: Returns the screenshot in base64 format

        >>> screenshot = GetScreenshotCommand()
    """
    screenshot = MOKO.Plugin("Clicker", "get", f"Screenshot", "string")
    return screenshot

def GetPngFileCommand() -> str:
    """
        This function returns png file in base64 format from the chosen png path

        :return: Returns png file in base64 format

        >>> png_file = GetPngFileCommand()
    """
    png_file = MOKO.Plugin("Clicker", "get", f"PngFile", "string")
    return png_file

def GetCoordinates() -> list:
    """
        This function returns coordinates (x,y)

        :return: Returns coordinates (x,y)

        >>> coordinates = GetCoordinates()
    """
    coordinates = MOKO.Plugin("Clicker", "get", f"Coordinates", "arrayint")
    return coordinates

