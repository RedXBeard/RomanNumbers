# -*- coding: utf-8 -*-
__author__ = "Barbaros Yıldırım (barbarosaliyildirim@gmail.com)"
__version__ = "0.1"
__date__ = "28 August 2014"

import re

class InvalidInputError(Exception): pass

BASE_ROMAN_NUMBERS = dict(M=1000, CM=900, D=500, CD=400, C=100,
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
                raise InvalidInputError, "Input has unqualified chars; '%s'" % message

    @staticmethod
    def check_for_romanchars(input):
        result = True, ""
        # chars has to be checked
        # if there is any unknown one according to the alphabet
        # defined globally
        acceptable_chars = BASE_ROMAN_NUMBERS.keys()
        unknown_chars = filter(lambda x: x not in acceptable_chars, input)
        # If there is any one, class initialization has to stop.
        # if not checking process should be continued with syntactically
        if unknown_chars:
            result = False, ", ".join(unknown_chars)
        else:
            result = RomanAlphabet.check_for_romansyntax(input)
        return result

    @staticmethod
    def check_for_romansyntax(input):
        result = True, ""
        # Regex used to check syntactically of given string
        pattern = re.compile("M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", re.VERBOSE)
        grouped = pattern.search(input).group()
        # if regex check returns partially or none
        # then means input is incorrect
        if grouped != input:
            result = False, input
        return result

    def convert_to_int(self):
        # TO-DO: implementation
        pass

    def convert_to_roman(self):
        # TO-DO: implementation
        pass
