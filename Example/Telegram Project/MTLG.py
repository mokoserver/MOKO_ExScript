import MOKO


def TelegramReport(name, mode, kind, data, valuetype='void'):
    MOKO.Telegram('alpha', 'set', '%E2%98%A0 MOKO SE REPORT\n'
                                  '------- DESCRIPTION --------\n'
                                  f'NAME: {name}\n'
                                  f'MODE: {mode}\n'
                                  f'KIND: {kind}\n'
                                  f'DATA: {data}\n'
                                  f'VALUETYPE: {valuetype}')

def TelegramMessenger(mode, head, body, valuetype='void', delaytime='void'):
    MOKO.Telegram('alpha', 'set', '%F0%9F%97%A8 MOKO SE MESSENGER\n'
                                  '------- DESCRIPTION --------\n'
                                  f'MODE: {mode}\n'
                                  f'HEAD: {head}\n'
                                  f'BODY: {body}\n'
                                  f'VALUETYPE: {valuetype}\n'
                                  f'DELAYTIME: {delaytime}')

def TelegramPlugin(name, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', '%E2%98%A0 MOKO SE PLUGIN\n'
                                  '------- DESCRIPTION --------\n'
                                  f'NAME: {name}\n'
                                  f'MODE: {mode}\n'
                                  f'COMMAND: {command}\n'
                                  f'VALUETYPE: {valuetype}')

def TelegramUtility(name, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', '%E2%98%A0 MOKO SE UTILITY\n'
                                  '------- DESCRIPTION --------\n'
                                  f'NAME: {name}\n'
                                  f'MODE: {mode}\n'
                                  f'COMMAND: {command}\n'
                                  f'VALUETYPE: {valuetype}')

def TelegramProgram(name, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', '%F0%9F%92%80 MOKO SE PROGRAM\n'
                                  '------- DESCRIPTION --------\n'
                                  f'NAME: {name}\n'
                                  f'MODE: {mode}\n'
                                  f'COMMAND: {command}\n'
                                  f'VALUETYPE: {valuetype}')

def TelegramClassic(role, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', '%F0%9F%92%A3 MOKO SE TELEGRAM\n'
                                  '------- DESCRIPTION --------\n'
                                  f'ROLE: {role}\n'
                                  f'MODE: {mode}\n'
                                  f'COMMAND: {command}\n'
                                  f'VALUETYPE: {valuetype}')

def TelegramDriver(name, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', '%E2%98%A0 MOKO SE DRIVER\n'
                                  '------- DESCRIPTION --------\n'
                                  f'NAME: {name}\n'
                                  f'MODE: {mode}\n'
                                  f'COMMAND: {command}\n'
                                  f'VALUETYPE: {valuetype}')

def TelegramStage(stage_string, type):
    MOKO.Telegram('alpha', 'set', '%E2%98%A0 MOKO SE STAGE\n'
                                  '------- DESCRIPTION --------\n'
                                  f'STAGE_STRING: {stage_string}\n'
                                  f'TYPE: {type}')

def TelegramEndScript(command='done'):
    TelegramProgram('script', 'set', command)