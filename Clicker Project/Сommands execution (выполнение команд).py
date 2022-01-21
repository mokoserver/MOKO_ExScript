import MOKO
from MOSC import stars

########## Commands ##########
#
# 1. Screenshot = MOKO.Plugin('ClickServer', 'get', 'Screenshot' ,'String') - take a screenshot of the screen (сделать скриншот экрана)
# 2. MOKO.Plugin('ClickServer', 'set', 'PngPath = C:\\MOKO SE\\Plugins\\MOKO ClickServer\\data\\Test2.bmp') - specify image path (указать путь картинки)
# 3. PngFile = MOKO.Plugin('ClickServer', 'get', 'GetPngFile' ,'String') - get image from specified path  (получить картинку по указанному пути)
# 4. MOKO.Plugin('ClickServer', 'set', 'MouseMove = 0 0') - move mouse cursor to coordinates (0,0) (переместить курсор мыши на координаты (0,0))
# 5. MOKO.Plugin('ClickServer', 'set', 'MouseLeftClick = 0 0') - pressing the left mouse button at coordinates (0,0) (нажатие левой кнопки мыши по координатам (0,0)
# 6. MOKO.Plugin('ClickServer', 'set', 'MouseRightClick = 0 0') - pressing the right mouse button at coordinates (0,0) (нажатие правой кнопки мыши по координатам (0,0)
# 7. MOKO.Plugin('ClickServer', 'set', 'MouseMiddleClick = 0 0') - pressing the middle mouse button at coordinates (0,0) (нажатие средней кнопки мыши по координатам (0,0)
# 8. Coordinates = MOKO.Plugin('ClickServer', 'get', 'GetCoordinates' ,'String') - get mouse cursor coordinates (получить координаты курсора мыши)
# 9. Minimize Window??

#Region Status (статус)
#description: Decribe;command;;(описание;команды);
#hesh The first command: to get a screenshot;of the screen;;(получить;скриншота;экрана)
Screenshot = MOKO.Plugin('ClickServer', 'get', 'Screenshot' ,'String')
MOKO.Report("expluginScr", 'set', 'picture', Screenshot)

MOKO.Program('tree', 'set', 'select = ' + 'The first command')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status (статус)

#Region Status (Статус)
#description: Decribe;command;;(описание;команды);
#hesh The second command: to specify the;image path;;(указать путь;картинки)
MOKO.Plugin('ClickServer', 'set', 'PngPath = C:\\MOKO SE\\Plugins\\MOKO ClickServer\\data\\Test2.bmp')

MOKO.Program('tree', 'set', 'select = ' + 'The second command')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

#Region Status (статус)
#description: Decribe;command;;(описание;команды);
#hesh The third command: to get the image;from the specified;path;(получить;картинку;по указанному;пути)
PngFile = MOKO.Plugin('ClickServer', 'get', 'GetPngFile' ,'String')
MOKO.Report("expluginFile", 'set', 'picture', PngFile)

MOKO.Program('tree', 'set', 'select = ' + 'The third command')
MOKO.Program('tree', 'set', 'chosen = passed')
MOKO.Program('tree', 'set', 'select = ' + 'третья команда')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status



MOKO.EndScript()