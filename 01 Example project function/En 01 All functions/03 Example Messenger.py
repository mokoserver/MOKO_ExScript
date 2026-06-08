import MOKO


MOKO.Stage('*Messenger*')
MOKO.MessageSet('Message 1',
                'Message №1. It has the type \'\'set\'\'. \n'
                'Displays a window with some title and content.\n'
                'Each message has a title and content that may be empty. \n'
                'After pressing the \'\'OK\'\' button, the message closes.',)

MOKO.MessageSet('Message 2',
                'Message №2. It has the type \'\'set\'\'.\n'
                'Has a timer after which the message closes.\n'
                'After pressing the \'\'OK\'\' button, the message will be closed \n'
                'regardless of whether the timer has expired.',
                '3')

c = MOKO.MessageGetString('Message 3',
                    'Message №3. It has the type \'\'get\'\'.\n'
                    'Gets data from a message of a specific type. \n'
                    'The default is \'\'void\'\'. Messages like \'\'get\'\' do not have a timer.')


MOKO.MessageSet( 'Message 4',
                 f'Message №4. You entered: {c}')

MOKO.ReportSetString('exmessenger',f'{c}')


b = MOKO.MessageGetString('Message 5',
                          'Message №5. It has the type \'\'get\'\'. \n'
                          'Retrieves \'\'string\'\' data from the message.\n')

MOKO.MessageSet('Message 6',
                f'Message №6. You entered: {b}')

MOKO.ReportSetString("exmessenger_1",
                     f'{b}')


a = MOKO.MessageGetBool('Messenger 7',
                        'Message №7. It has the type \'\'get\'\'. \n'
                              'Retrieves boolean data from the message. \n'
                              'When you click on the \'\'Yes\'\' button, returns True, \n'
                              'when you click on \'\'No\'\', it returns False.',
                        False)


MOKO.Stage(f'{a}')

if a:
    MOKO.MessageSet('True',
                    'You clicked on the \'\'Yes\'\' button.')
    MOKO.ReportSetString("exmessenger_2",
                         'True')
else:
    MOKO.MessageSet('False',
                    'You clicked on the \'\'No\'\' button.')
    MOKO.ReportSetString("exmessenger_2",
                         'False')

MOKO.ReportSetString("exmessenger_3",
                      'The script completed successfully.')


MOKO.ScriptEnd()