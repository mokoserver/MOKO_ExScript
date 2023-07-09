import MOKO


# Library version 2.10.24.1
# Added commands description at 24.10.2022

# **init**
# ClickerInit() - this function initializes plugin MOKO Clicker
# **set**
# MouseLeftClick() - this function imitates pressing mouse left button
# MouseRightClick() - this function imitates pressing mouse right button
# MouseMiddleClick() - this function imitates pressing mouse middle button
# MouseMove() - this function moves mouse cursor to the point (x,y)
# Screenshot() - this function makes a screenshot
# PngPath() - this function sets a path to the png file
# **get**
# GetScreenshot() - this function makes a screenshot and returns it in base64 format
# GetPngFile() - this function returns png file in base64 format from the chosen png path
# GetCoordinates() - this function returns coordinates (x,y)


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

    # The next code strings was commented because of inoperability
    # processes = Popen('tasklist', stdin=PIPE, stderr=PIPE, stdout=PIPE).communicate()[0]
    # while processes.find("MOKO Clicker".encode("utf8")) == -1:
    #     MOKO.Stage("Waiting for the plugin to run...")
    #     processes = Popen('tasklist', stdin=PIPE, stderr=PIPE, stdout=PIPE).communicate()[0]


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


def MouseLeftClick(x:int, y:int) -> None:
    """
        This function imitates pressing mouse left button

        :param x: axis Ox value
        :param y: axis Oy value

        :return: None

        >>> MouseLeftClick(1000, 2000)
        >>> MouseLeftClick("1000", "2000")
    """
    MOKO.Plugin("Clicker", "set", f"MouseLeftClick = {x} {y}")
    return None

def MouseRightClick(x:int, y:int) -> None:
    """
        This function imitates pressing mouse right button

        :param x: axis Ox value
        :param y: axis Oy value

        :return: None

        >>> MouseRightClick(1000, 2000)
        >>> MouseRightClick("1000", "2000")
    """
    MOKO.Plugin("Clicker", "set", f"MouseRightClick = {x} {y}")

def MouseMiddleClick(x:int, y:int) -> None:
    """
        This function imitates pressing mouse middle button

        :param x: axis Ox value
        :param y: axis Oy value

        :return: None

        >>> MouseMiddleClick(1000, 2000)
        >>> MouseMiddleClick("1000", "2000")
    """
    MOKO.Plugin("Clicker", "set", f"MouseMiddleClick = {x} {y}")

def MouseMove(x:int, y:int) -> None:
    """
        This function moves mouse cursor to the point (x,y)

        :param x: axis Ox value
        :param y: axis Oy value

        :return: None

        >>> MouseMove(1000, 2000)
        >>> MouseMove("1000", "2000")
    """
    MOKO.Plugin("Clicker", "set", f"MouseMove = {x} {y}")

def Screenshot() -> None:
    """
        This function makes a screenshot. The screenshot is saved in "C:/MOKO SE/Plugins/MOKO Clicker/screenshots/"

        :return: None

        >>> Screenshot()
    """
    MOKO.Plugin("Clicker", "set", f"Screenshot")

def PngPath(path:str) -> None:
    """
        This function sets a path to the png file

        :return: None

        >>> PngPath("C:/MOKO SE/Plugins/MOKO Clicker/screenshots/Clicker.png")
    """
    MOKO.Plugin("Clicker", "set", f"PngPath = {path}")


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

def GetScreenshot() -> str:
    """
        This function makes a screenshot and returns it in base64 format

        :return: Returns the screenshot in base64 format

        >>> screenshot = GetScreenshot()
    """
    screenshot = MOKO.Plugin("Clicker", "get", f"Screenshot", "string")
    return screenshot

def GetPngFile() -> str:
    """
        This function returns png file in base64 format from the chosen png path

        :return: Returns png file in base64 format

        >>> png_file = GetPngFile()
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

