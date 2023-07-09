import MOKO as Moko

language = Moko.Report("language", 'get', 'string', 'string', 'string')

if language == 'English(default)':
    Moko.Stage('*Messenger*')
    Moko.Messenger('set', 'Messenger_1', 'Message №1. It has the type \'\'set\'\'. Displays a window with some title and '
                                         'content. Each message has a title and content that may be empty. '
                                         'After pressing the \'\'OK\'\' button, the message closes.')
    Moko.Messenger('set', 'Messenger_2', 'Message №2. It has the type \'\'set\'\'. Has a timer after which the message closes'
                                         '. After pressing the \'\'OK\'\' button, the message will be closed regardless of '
                                         'whether the timer has expired.', 'void', str(5))
    c = Moko.Messenger('get', 'Messenger_3', 'Message №3. It has the type \'\'get\'\'. Gets data from a message of a specific'
                                             'type. The default is \'\'void\'\'. Messages like \'\'get\'\' do not have a timer.',
                                             'string')
    Moko.Messenger('set', 'Messenger_4', 'Message №4. You entered: ' + c)
    Moko.Report("exmessenger", 'set', 'string', c)
    b = Moko.Messenger('get', 'Messenger_5', 'Message №5. It has the type \'\'get\'\'. '
                                             'Retrieves \'\'string\'\' data from the message.', 'string')
    Moko.Messenger('set', 'Messenger_6', 'Message №6. You entered: ' + b)
    Moko.Report("exmessenger_1", 'set', 'string', b)
    a = Moko.Messenger('get', 'Messenger_7', 'Message №7. It has the type \'\'get\'\'. '
                                             'Retrieves boolean data from the message. '
                                             'When you click on the \'\'Yes\'\' button, returns True, when you click on \'\'No\'\','
                                             ' it returns False.', 'boolean')
    if a == True:
        Moko.Messenger('set', 'True', 'You clicked on the \'\'Yes\'\' button.')
        Moko.Report("exmessenger_2", 'set', 'string', 'True')
    else:
        Moko.Messenger('set', 'False', 'You clicked on the \'\'No\'\' button.')
        Moko.Report("exmessenger_2", 'set', 'string', 'False')
    Moko.Report("exmessenger_3", 'set', 'string', 'The script completed successfully.')

elif language == 'Русский':
    Moko.Stage('*Messenger*')
    Moko.Messenger('set', 'Сообщение №1', 'Сообщение №1. Есть  функция \'\'set\'\'  . Она отображает окно с некоторым заголовком и '
                                     'содержанием. У каждого сообщения есть заголовок и содержимое, которое может быть пустым. После нажатия '
                                     'на кнопу \'\'OK\'\', сообщение закроется.')
    Moko.Messenger('set', 'Сообщение №2', 'Сообщение №2. Так же есть фунция \'\'set\'\'. Она имеет таймер, по истечении которого сообщение закрывается. '
                                     'После нажатия на кнопку \'\'OK\'\', сообщение будет закрыто независимо от того,'
                                     'истек ли таймер.', 'void', str(6))
    c = Moko.Messenger('get', 'Сообщение №3', 'Сообщение №3. Есть функция \'\'get\'\'. Она получает данные из сообщения определённого '
                                         'типа. По умолчанию это функция \'\'void\'\'. Сообщение с типом фунции \'\'get\'\' не имеет данных.',
                   'string')
    Moko.Messenger('set', 'Сообщение №4', 'Сообщение №4. Вы ввели: ' + c)
    Moko.Report("exmessenger", 'set', 'string', c)
    b = Moko.Messenger('get', 'Сообщение №5', 'Сообщение №5. Так же есть функция \'\'get\'\'. Она извлекает тип данных \'\'string\'\' из сообщения.', 'string')
    Moko.Messenger('set', 'Сообщение №6', 'Сообщение №6. Вы ввели: ' + b)
    Moko.Report("exmessenger_1", 'set', 'string', b)
    a = Moko.Messenger('get', 'Сообщение №7', 'Сообщение №7. Он имеет тип \'\'get\'\'. Извлекает логические данные из сообщения. '
                                         'Когда вы нажимаете на кнопу \'\'Yes\'\', возвращается значение True, когда вы нажимаете кнопку \'\'No\'\', '
                                         'возвращается значение False.', 'boolean')
    if a == True:
        Moko.Messenger('set', 'True', 'Вы нажали на кнопку \'\'Yes\'\' .')
        Moko.Report("exmessenger_2", 'set', 'string', 'True')
    else:
        Moko.Messenger('set', 'False', 'Вы нажали на кнопку \'\'No\'\' .')
    Moko.Report("exmessenger_2", 'set', 'string', 'False')
    Moko.Report("exmessenger_3", 'set', 'string', 'Скрипт успешно завершён.')


Moko.EndScript()