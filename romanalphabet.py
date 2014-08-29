# -*- coding: utf-8 -*-
__author__ = "Barbaros Yıldırım (barbarosaliyildirim@gmail.com)"
__version__ = "0.1"
__date__ = "28 August 2014"

import re

class InvalidInputError(Exception): pass
class ConvertionError(Exception): pass

BASE_ROMAN_NUMBERS = dict(M=1000, CM=900, D=500, CD=400, C=100, XC=90,
                          L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1)

class RomanAlphabet(object):

    def __init__(self, input):
        self.input = str(input).upper()
        self.int = None
        self.roman = None
        # If input is an integer ...
        if str(self.input).isdigit():
            self.int = self.input
        # ... Otherwise has to be checked
        if not self.int:
            result, message = RomanAlphabet.check_for_romanchars(self.input)
            if result:
                self.roman = self.input
            else:
                raise InvalidInputError, \
                        "Input has unqualified chars; '%s'" % message

    @staticmethod
    def check_for_romanchars(input):
        """ To check alphabet and give exact unmatched ones. """
        result = True, ""
        # chars has to be checked
        # if there is any unknown one according to the alphabet
        # defined globally.
        acceptable_chars = BASE_ROMAN_NUMBERS.keys()
        unknown_chars = filter(lambda x: x not in acceptable_chars, input)
        # If there is any one, class initialization has to stop.
        # if not checking process should be continued with syntactically.
        if unknown_chars:
            result = False, ", ".join(unknown_chars)
        else:
            result = RomanAlphabet.check_for_romansyntax(input)
        return result

    @staticmethod
    def check_for_romansyntax(input):
        """ syntactically check if given number for roman numeral system. """
        result = True, ""
        # Regex used to check syntactically of given string
        pattern = re.compile("""M*(CM|CD|D?C{0,3})
                                (XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$""",
                             re.VERBOSE)
        grouped = pattern.search(input).group()
        # if regex check returns partially or none
        # then means input is incorrect
        if grouped != input:
            result = False, input
        return result

    def convert_to_int(self):
        """ To represent roman numeral systemed value with in integer. """
        # If the class is generated with an integer then
        # that can be the result as well.
        result = 0
        if self.int:
            result = self.int
        else:
            # Reversed sum has been considered
            # by this way, pre roman char can be considered
            # so current one can be checked whether
            # related value should be added or extracted.
            pre = 0
            for i in range(len(self.roman)-1, -1, -1):
                tmp = BASE_ROMAN_NUMBERS[self.roman[i]]
                if tmp < pre:
                    result -= tmp
                else:
                    result += tmp
                pre = tmp
        self.int = result
        return self.int

    def convert_to_roman(self):
        """ To represent integer value with in roman number system. """
        result = ""
        # If the class is generated with in roman numeral system
        # then that can be the result as well.
        if self.roman:
            result = self.roman
        else:
            # To divide given integer input with an
            # order base on roman alphabet,
            # dict must be converted into an ordered list
            base_sorted_numbers = sorted(BASE_ROMAN_NUMBERS.items(),
                                         key=lambda x: x[1], reverse=True)
            input = int(self.int)
            # Each roman char's integer representation considered,
            # according to the division result returned value generated.
            for rnumber, number in base_sorted_numbers:
                count = input / number
                result += rnumber * count
                input -= count * number
        # To be sure generated representation whether correct or not.
        if RomanAlphabet.check_for_romansyntax(result):
            self.roman = result
        else:
            raise ConvertionError, 'Error occured while conversion'
        return self.roman
