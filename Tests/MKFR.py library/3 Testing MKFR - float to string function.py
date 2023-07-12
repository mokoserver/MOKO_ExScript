import MOKO
import MFRT

MOKO.Messenger("set", "Testing MFRT function convert float to string#@notes",
               "This script demonstrates how to convert a float, int or string to a string of "
               "the given format. The format is specified using the reference number")

MOKO.Messenger("set", "Description#@links",
               "Value: translated value\n"
               "Reference number: a string number that will be the template to be converted\n"
               "Resolution: the number of zeros in the fractional part\n"
               "Delimiter: separator between number and fractional part\n"
               "Prefix: separator between number and fractional part")

test_list_reference_number = ["100.00000u", "100.0000u", "100.000u", "100.00u", "100.0u", "100u",
                              "100.00000m", "100.0000m", "100.000m", "100.00m", "100.0m", "100m",
                              "100.00000",  "100.0000",  "100.000",  "100.00",  "100.0",  "100",
                              "100.00000k", "100.0000k", "100.000k", "100.00k", "100.0k", "100k",
                              "100.00000M", "100.0000M", "100.000M", "100.00M", "100.0M", "100M"]

MOKO.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: str\n"
               "Reference number: str\n"
               "Resolution: None\n"
               "Prefix: None\n"
               "Delimeter: None")

MOKO.Report('StringConvertingRefNumber', 'info', 'table', 'Input value#130;'
                                                          'Reference number#130;'
                                                          'Resolution#75;'
                                                          'Prefix#50;'
                                                          'Delimiter#75;'
                                                          'Output value#130;')

resolution = prefix = delimiter = '-'

test_list_value = ["100m", "100", "100k"]

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number)
        MOKO.Report('StringConvertingRefNumber', 'set', 'table', f'{input_value};'
                                                                 f'{reference_number};'
                                                                 f'{resolution};'
                                                                 f'{prefix};'
                                                                 f'{delimiter};'
                                                                 f'{output_value};')

MOKO.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: float\n"
               "Reference number: str\n"
               "Resolution: None\n"
               "Prefix: None\n"
               "Delimeter: None")

MOKO.Report('FloatConverting', 'info', 'table', 'Input value#130;'
                                                'Reference number#130;'
                                                'Resolution#75;'
                                                'Prefix#50;'
                                                'Delimiter#75;'
                                                'Output value#130;')

test_list_value = [0.001, 100.001]

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number)
        MOKO.Report('FloatConvertingRefNumber', 'set', 'table', f'{input_value};'
                                                                f'{reference_number};'
                                                                f'{resolution};'
                                                                f'{prefix};'
                                                                f'{delimiter};'
                                                                f'{output_value};')

MOKO.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: int\n"
               "Reference number: str\n"
               "Resolution: None\n"
               "Prefix: None\n"
               "Delimeter: None")

test_list_value = [0, 100]

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number)
        MOKO.Report('IntegerConvertingRefNumber', 'set', 'table', f'{input_value};'
                                                                  f'{reference_number};'
                                                                  f'{resolution};'
                                                                  f'{prefix};'
                                                                  f'{delimiter};'
                                                                  f'{output_value};')

MOKO.Messenger("set", "Message#@notes",
               "Start translated value into:\n"
               "Value: int\n"
               "Reference number: str\n"
               "Resolution: int\n"
               "Prefix: None\n"
               "Delimeter: None")

test_list_value = [0, 100]

for input_value in test_list_value:
    for reference_number in test_list_reference_number:
        output_value = MFRT.ConvertFloatToString(input_value, reference_number)
        MOKO.Report('IntegerConvertingRefNumber', 'set', 'table', f'{input_value};'
                                                                  f'{reference_number};'
                                                                  f'{resolution};'
                                                                  f'{prefix};'
                                                                  f'{delimiter};'
                                                                  f'{output_value};')

MOKO.EndScript()