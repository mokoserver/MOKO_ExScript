import MokoRequestLib as Moko


def stars(word):
    """Заполняет строку звездочками"""
    formated_string = '{:*^60}'.format(word)
    return formated_string


def choice_language():
    language = Moko.Messenger('get', 'Language', 'Please select your language in dropdown:', 'choice=English (default);Russian')
    return language

