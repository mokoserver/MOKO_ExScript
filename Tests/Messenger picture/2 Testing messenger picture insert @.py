import MOKO

#Region Status
#hesh Messenger Testing

MOKO.Stage('mode -> set, head -> Attention#@attention')
MOKO.Messenger('set', 'Attention#@attention',
               'To insert an image, after the head name, write #@attention', delaytime='5')

MOKO.Stage('mode -> set, head -> Bye#@bye')
MOKO.Messenger('set', 'Bye#@bye',
               'To insert an image, after the head name, write #@bye', delaytime='5')

MOKO.Stage('mode -> set, head -> Call#@call')
MOKO.Messenger('set', 'Call#@call',
               'To insert an image, after the head name, write #@call', delaytime='5')

MOKO.Stage('mode -> set, head -> Callback#@callback')
MOKO.Messenger('set', 'Callback#@callback',
               'To insert an image, after the head name, write #@callback', delaytime='5')

MOKO.Stage('mode -> set, head -> Clear#@clear')
MOKO.Messenger('set', 'Clear#@clear',
               'To insert an image, after the head name, write #@clear', delaytime='5')

MOKO.Stage('mode -> set, head -> Delete#@delete')
MOKO.Messenger('set', 'Delete#@delete',
               'To insert an image, after the head name, write #@delete', delaytime='5')

MOKO.Stage('mode -> set, head -> Failed#@failed')
MOKO.Messenger('set', 'Failed#@failed',
               'To insert an image, after the head name, write #@failed', delaytime='5')

MOKO.Stage('mode -> set, head -> File#@file')
MOKO.Messenger('set', 'File#@file',
               'To insert an image, after the head name, write #@file', delaytime='5')

MOKO.Stage('mode -> set, head -> Hello#@hello')
MOKO.Messenger('set', 'Hello#@hello',
               'To insert an image, after the head name, write #@hello', delaytime='5')

MOKO.Stage('mode -> set, head -> Idea#@idea')
MOKO.Messenger('set', 'Idea#@idea',
               'To insert an image, after the head name, write #@idea', delaytime='5')

MOKO.Stage('mode -> set, head -> Insert#@insert')
MOKO.Messenger('set', 'Insert#@insert',
               'To insert an image, after the head name, write #@insert', delaytime='5')

MOKO.Stage('mode -> set, head -> Language#@language')
MOKO.Messenger('set', 'Language#@language',
               'To insert an image, after the head name, write #@language', delaytime='5')

MOKO.Stage('mode -> set, head -> Link#@link')
MOKO.Messenger('set', 'Link#@link',
               'To insert an image, after the head name, write #@link', delaytime='5')

MOKO.Stage('mode -> set, head -> Notes#@notes')
MOKO.Messenger('set', 'Notes#@notes',
               'To insert an image, after the head name, write #@notes', delaytime='5')

MOKO.Stage('mode -> set, head -> Punk#@punk')
MOKO.Messenger('set', 'Punk#@punk',
               'To insert an image, after the head name, write #@punk', delaytime='5')


MOKO.Stage('mode -> set, head -> Repeat#@repeat')
MOKO.Messenger('set', 'Repeat#@repeat',
               'To insert an image, after the head name, write #@repeat', delaytime='5')


MOKO.Stage('mode -> set, head -> Save#@save')
MOKO.Messenger('set', 'Save#@save',
               'To insert an image, after the head name, write #@save', delaytime='5')


MOKO.Stage('mode -> set, head -> Time#@time')
MOKO.Messenger('set', 'Time#@time',
               'To insert an image, after the head name, write #@time', delaytime='5')


MOKO.Stage('mode -> set, head -> Warning#@warning')
MOKO.Messenger('set', 'Warning#@warning',
               'To insert an image, after the head name, write #@warning', delaytime='5')

MOKO.Program('tree', 'set', 'select = ' + 'Messenger Testing')
MOKO.Program('tree', 'set', 'chosen = passed')

#EndRegion Region Status
MOKO.EndScript()