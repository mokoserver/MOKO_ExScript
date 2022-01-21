import MOKO

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


MOKO.EndScript()