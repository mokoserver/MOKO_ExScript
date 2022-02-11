import MOKO
from MOSC import stars

MOKO.Stage(stars('*'))
MOKO.Stage(stars('MOKO Clicker'))
MOKO.Stage(stars('*'))

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

language = MOKO.Messenger('get', 'Language. Язык.jpg', 'Please select your language in dropdown.\nПожалуйста, выберите свой язык в раскрывающемся списке:',
                          'choice=English;Русский;')
MOKO.Report("language", 'set', 'string', language)

#Region Choice language (выбор языка)
#hesh Language
MOKO.Program('tree', 'set', 'select = ' + 'Language')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Choice language

if language == 'English':
    MOKO.Messenger('set', 'Greeting.jpg',
                   'This presentation will show 3 commands, but there are more commands. '
                   'The first command is to get a screenshot of the screen, '
                   'the second command is to specify the image path and '
                   'the last command is to get the image from the specified path.')
elif language == 'Русский':
    MOKO.Messenger('set', 'Greeting.jpg',
                   'В данном презентации будут показаны 3 команды, но команд больше. '
                   'Первая команда - получение скриншота экрана, '
                   'вторая команда - указание пути картинки, '
                   'последняя команда - получение картинки по указанному пути.')


#Region Status (статус)
#hesh Greeting
MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()