import MOKO

def WriteGraphCommand():
    """
        Show lines in the graph

        :return: None
    """
    MOKO.Plugin('Graph', 'set', "Write Graph")
    return None

def AddLineCommand(name, ArrOy, ArrOx, LineWidth="3", Color="000000", Visible="True"):
    """
        This function adds a line in the plugin memory

        :param name: name of the line
        :param ArrOy: array of points for axis Oy
        :param ArrOx:  array of points for axis Ox
        :param LineWidth: width of the line
        :param Color: color of the line. Color is transmitted in hexadecimal representation (FFFFFF - white)
        :param Visible: visible of the line: True, False, Yes or No

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Add Line={name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    MOKO.Plugin('Graph', 'set', "Write Graph")
    return None

def ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth="3", Color="000000", Visible="True"):
    """
        This function changes the line which has already added

        :param numLine: serial number or name of the line, which an user wants to change. The numbers begin with 0.
                        Also the user can pass the name of the line
        :param name: new name of the line
        :param ArrOy: new array of points for axis Oy
        :param ArrOx:  new array of points for axis Ox
        :param LineWidth: new width of the line
        :param Color: new color of the line. Color is transmitted in hexadecimal representation (FFFFFF - white)
        :param Visible: new parameter of visible of the line: True, False, Yes or No

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Change Line={numLine};{name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    return None

def DeleteLineCommand(numLine):
    """
        This function deletes lines

        :param numLine: serial number or name of the line, which an user wants to delete. The numbers begin with 0.
                        Also the user can pass a list of lines' numbers or names. If the user wants to delete all lines,
                        he can pass "All"

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Delete Line={numLine}")
    return None

def HideLineCommand(numLine):
    """
        This function hides lines

        :param numLine: serial number or name of the line, which an user wants to hide. The numbers begin with 0.
                        Moreover the user can pass a list of lines' numbers or names. If the user wants to hide all lines,
                        he can pass "All"

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Hide Line={numLine}")
    return None

def ShowLineCommand(numLine):
    """
        This function shows lines

        :param numLine: serial number or name of the line, which an user wants to show. The numbers begin with 0.
                        Moreover the user can pass a list of lines' numbers or names. If the user wants to show all lines,
                        he can pass "All"

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Show Line={numLine}")
    return None

def ShowLineOnlyCommand(numLine):
    """
        This function shows only chosen lines

        :param numLine: serial number or name of the line, which an user wants to show. The numbers begin with 0.
                        Moreover the user can pass a list of lines' numbers or names. The chosen lines will be shown
                        and the others will be hidden

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Show Line=Only;{numLine}")
    return None

def AddGraphSettCommand(Value_OyOx, Name_Oy, Name_Ox, Autoscale="Yes"):
    """
        This function sets graph settings

        :param Value_OyOx: the list of [min,max,min,max] values of axises Oy and Ox respectively
        :param Name_Oy: the name of axis Oy
        :param Name_Ox: the name of axis Ox
        :param Autoscale: the parameter of the graph scaling. It can be:
                          OnlyOy - scaling only axis Oy;
                          OnlyOx - scaling only axis Ox;
                          No - off scaling;
                          Yes - on scaling

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Add Graph Settings={Value_OyOx};{Name_Oy};{Name_Ox};{Autoscale}")
    return None

def AutoscaleCommand(command="Yes"):
    """
        This function sets autoscale

        :param command: the parameter of the graph scaling. It can be:
                          OnlyOy - scaling only axis Oy;
                          OnlyOx - scaling only axis Ox;
                          No - off scaling;
                          Yes - on scaling

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Autoscale={command}")
    return None

def ScreenshotWindowCommand():
    """
        This function make a screenshot of the plugin front panel. The screenshot is saved
        in "C:\MOKO SE\Plugins\MOKO Graph\screenshots\

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Screenshot Window")
    return None

def ScreenshotGraphCommand():
    """
        This function make a screenshot of the graph front panel. The screenshot is saved
        in "C:\MOKO SE\Plugins\MOKO Graph\screenshots\

        :return: None
    """
    MOKO.Plugin('Graph', 'set', f"Screenshot Graph")
    return None

def GetScreenshotWindow():
    """
        This function make a screenshot of the plugin front panel and returns it in base64 format. The screenshot is saved
        in "C:\MOKO SE\Plugins\MOKO Graph\screenshots\

        :return: Returns the screeshot in base64 format
    """
    screen = MOKO.Plugin('Graph', 'get', f"ScreenshotWindow", 'string')
    return screen

def GetScreenshotGraph():
    """
        This function make a screenshot of the graph front panel and returns it in base64 format. The screenshot is saved
        in "C:\MOKO SE\Plugins\MOKO Graph\screenshots\

        :return: Returns the screeshot in base64 format
    """
    screen = MOKO.Plugin('Graph', 'get', f"ScreenshotGraph", 'string')
    return screen

def LegendCommand():
    """
        This function hide or show the graph legend. If there are no lines in the graph, legend won't be shown

        :return: None
    """
    MOKO.Plugin('Graph', 'set', "Legend")
    return None

def ClearGraphCommand():
    """
        This function clear the graph

        :return: None
    """
    MOKO.Plugin('Graph', 'set', "Clear Graph")
    return None