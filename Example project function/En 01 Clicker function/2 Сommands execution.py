import MOKO
import MCLK


MCLK.ClickerInit()

#Region Status
#description: Decribe;command;
#hesh The first command: to get a screenshot;of the screen;
screenshot = MCLK.GetScreenshot()
MOKO.Report("ClickerScr", 'set', 'picture', screenshot)

MOKO.Program('tree', 'set', 'select = ' + 'The first command')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

#Region Status
#description: Decribe;command;
#hesh The second command: to specify the;image path;

MCLK.PngPath("C:/MOKO SE/Images/Desktop MOKO Long.png")

MOKO.Program('tree', 'set', 'select = ' + 'The second command')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

#Region Status (статус)
#description: Decribe;command;
#hesh The third command: to get the image;from the specified;path
png_file = MCLK.GetPngFile()
MOKO.Report("ClickerFile", 'set', 'picture', png_file)

MOKO.Program('tree', 'set', 'select = ' + 'The third command')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status



MOKO.EndScript()