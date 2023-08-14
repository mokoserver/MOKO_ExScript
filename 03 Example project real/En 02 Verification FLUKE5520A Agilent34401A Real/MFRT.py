def ConvertStringToFloat(value: str):
    """
        This function calls the transfer function from the СI system to the normal system

        :param value: str variable: input variable
        :return: translation value in type float
    """
    if type(value) != str:
        return float(value)
    mfrt = MFRTLibrary(value=value)
    return mfrt.GetPrefixInValue()


def ConvertFloatToString(value: (float | str | int), reference_number: str = None, resolution: int = None,
                         delimiter: str = None, prefix: str = None):
    """
        This function calls the transfer function from the normal system to the CI system

        :param value: float, string and int variable: translated number
        :param reference_number: string variable: a string number that will be the template to be converted
        :param resolution: integer variable: the number of zeros in the fractional part. Defaults to None
        :param delimiter: string variable: separator between number and fractional part. Defaults to None
        :param prefix: string variable: separator between number and fractional part. Defaults to None
        :return: translation value for output in definition
    """
    mfrt = MFRTLibrary(value=value, reference_number=reference_number, resolution=resolution, delimiter=delimiter,
                       prefix=prefix)
    return mfrt.TranslateValue()


#######################################################################################################################


class MFRTLibrary:
    def __init__(self, value: (float | str | int), reference_number: str = None, resolution: int = None,
                 delimiter: str = None, prefix: str = None):

        self.__value = value
        self.__reference_number = reference_number
        self.__resolution = resolution
        self.__delimiter = delimiter
        self.__prefix = prefix
        self.__prefix_value = None
        self.__get_prefix, self.__check = False, False
        self.__translate_value = self.__reference_number if self.__reference_number else self.__value
        self.__list_prefix_english = ['P', 'T', 'G', 'M', 'k', '-', 'm', 'u', 'n', 'p', 'f']
        self.__list_prefix_russian = ['П', 'Т', 'Г', 'М', 'к', '-', 'м', 'мк', 'н', 'п', 'ф']

    def GetPrefixInValue(self):
        """
            The function of converting a number to normal form and the function of obtaining a prefix

            :return: a float number if the function was called to translate a number, otherwise returns the
            prefix of the number
        """

        if self.__translate_value[-2:] in self.__list_prefix_english + self.__list_prefix_russian:
            ind = 2
        elif self.__translate_value[-1:] in self.__list_prefix_english + self.__list_prefix_russian:
            ind = 1
        else:
            ind = 0
        self.__prefix_value = self.__translate_value[-ind:] if ind != 0 else '-'
        self.__get_delimiter_value(ind=ind)
        try:
            self.__translate_value = float(self.__translate_value)
        except ValueError:
            return self.__value
        if self.__get_prefix:
            self.__get_prefix = False
            return self.__prefix_value
        self.__translate_value = self.__translate_value * self.__CreateTranslationConstant()
        return float(f'{self.__translate_value:.14f}')

    def __CreateTranslationConstant(self):
        """
            The function of obtaining a float value, increasing or decreasing the translated number by the number of times

            :return: a float value in which it is worth increasing or decreasing the number for translation
        """
        if self.__prefix_value in self.__list_prefix_english and self.__prefix_value != '-':
            list_prefix = self.__list_prefix_english
        elif self.__prefix_value in self.__list_prefix_russian and self.__prefix_value != '-':
            list_prefix = self.__list_prefix_russian
        else:
            return 1.0
        index = list_prefix.index(self.__prefix_value)
        len_lst_prefix = len(list_prefix)
        const_resolution = (len_lst_prefix // 2 - index) * 3
        return round(10 ** const_resolution, (len(list_prefix) - 1) // 2 * 3)

    def TranslateValue(self):
        """
            Function to convert from float or int to CI

            :return: translation value for output in definition
        """
        if not self.__reference_number and not self.__resolution and not self.__delimiter and not self.__prefix:
            return str(self.__value)
        if isinstance(self.__value, (float | int)):
            if isinstance(self.__value, int):
                self.__value = f'{float(self.__value):.14f}'.split('.')[0]
            else:
                if 'e' in str(self.__value) and not self.__resolution and not self.__reference_number:
                    self.__resolution = int(str(self.__value)[-2:])
                elif not self.__resolution and not self.__reference_number:
                    self.__resolution = len(str(self.__value).split('.')[1])
                self.__value = f'{float(self.__value):.14f}'
                self.__value = self.__value.split('.')[0] + '.' + self.__value.split('.')[1]
        elif isinstance(self.__value, str) and not self.__reference_number and not self.__resolution:
            delimiter_value = next((x for x in self.__value[1:] if not x.isdigit() and not x.isalpha()), None)
            if delimiter_value:
                self.__resolution = len(self.__value.split(delimiter_value)[1])
            else:
                self.__resolution = 0
        if not self.__reference_number:
            self.__check = True
            if self.__check_prefix_in_value():
                try:
                    float(self.__value)
                except ValueError:
                    self.__translate_value = self.__value
                    self.__value = self.GetPrefixInValue()
                return self.__CheckZerosAfterPointInString()
            return self.__value
        else:
            if not self.__prefix:
                self.__get_prefix = True
                self.__prefix = self.GetPrefixInValue()
            else:
                self.__check = True
                if not self.__check_prefix_in_value():
                    return self.__value
            self.__check_prefix_in_value()
            return self.__TranslateVariableReferenceNumberAndPrefix()

    def __TranslateVariableNotReferenceNumber(self):
        """
             Function to convert from value in out format when absent reference_number

             :return: translated number
        """
        if self.__resolution:
            self.__delimiter = next((x for x in self.__value[1: len(self.__value)] if not x.isdigit()), None)
            self.__get_prefix = True
            self.__translate_value = self.__value
            self.__prefix = self.GetPrefixInValue()
            if self.__delimiter:
                self.__value = self.__value.replace(self.__delimiter, '.')
                self.__value = self.__value[:-len(self.__prefix)] if self.__prefix != '-' else self.__value
            self.__value = f'{float(self.__value):.14f}'.split('.')
            return self.__value[0] + f"{self.__delimiter if self.__delimiter else '.'}" + \
                self.__value[1][:self.__resolution]
        else:
            return self.__value

    def __TranslateVariableReferenceNumberAndPrefix(self):
        """
            Function to convert from value in out format when there is a reference_number

            :return: translated number
        """
        if self.__prefix:
            self.__translate_value = self.__value
            self.__value = self.GetPrefixInValue()
            delimiter_reference_number = next((x for x in self.__reference_number[1: -(len(self.__prefix))]
                                               if not x.isdigit()), None)
            if not self.__delimiter and not delimiter_reference_number:
                return self.__CheckZerosAfterPointInString()
            self.__delimiter = self.__delimiter if self.__delimiter else delimiter_reference_number
            if not self.__resolution:
                if self.__prefix != "-" and delimiter_reference_number:
                    self.__resolution = len(self.__reference_number.split(delimiter_reference_number)[1]) - len(
                        self.__prefix)
                elif delimiter_reference_number:
                    self.__resolution = len(self.__reference_number.split(delimiter_reference_number)[1])
                else:
                    self.__resolution = 0
            return self.__CheckZerosAfterPointInString()
        return self.__TranslateVariableNotReferenceNumber()

    def __CheckZerosAfterPointInString(self):
        """
            Converting a number from float to string

            :return: translation value for output in definition
        """
        if self.__prefix:
            self.__prefix_value = self.__prefix
        translation_cost = self.__CreateTranslationConstant()
        translation_value = float(float(self.__value) / translation_cost)
        formatted_translation_value = f'{translation_value:.14f}'.split('.')
        if not self.__prefix:
            self.__prefix = ''
        else:
            self.__prefix = '' if self.__prefix in '-' or not self.__prefix_value else self.__prefix
        if not self.__delimiter or not self.__resolution:
            if self.__resolution:
                return formatted_translation_value[0] + '.' + formatted_translation_value[1][:self.__resolution] + \
                    self.__prefix
            return formatted_translation_value[0] + self.__prefix
        if len(formatted_translation_value[1]) < self.__resolution:
            self.__resolution = len(formatted_translation_value[1])
        return formatted_translation_value[0] + self.__delimiter + formatted_translation_value[1][:self.__resolution] + \
            self.__prefix

    def __check_prefix_in_value(self):
        if self.__check:
            self.__check = False
            if (self.__prefix not in self.__list_prefix_english + self.__list_prefix_russian) and self.__prefix:
                return False
            return True
        if self.__prefix in self.__list_prefix_english:
            self.__list_prefix = self.__list_prefix_english
        else:
            self.__list_prefix = self.__list_prefix_russian

    def __get_delimiter_value(self, ind: int = None):
        delimiter_value = next((x for x in self.__translate_value[1: -(len(self.__prefix_value))] if not x.isdigit()),
                               None)
        self.__translate_value = self.__translate_value[:-ind] if ind != 0 else self.__translate_value
        if delimiter_value:
            self.__translate_value = self.__translate_value.replace(delimiter_value, '.')
