# -*- coding: utf-8 -*-
__author__ = "Barbaros Yıldırım (barbarosaliyildirim@gmail.com)"
__version__ = "1.1"
__date__ = "28 August 2014"

import re

class InvalidInputError(Exception): pass
class ConvertionError(Exception): pass

BASE_ROMAN_NUMBERS = dict(M=1000, CM=900, D=500, CD=400, C=100, XC=90,
                          L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1)

class RomanAlphabet(object):

    def __init__(self, input):
        self.input = str(input).upper()
        # If input is an integer ...
        if not str(self.input).isdigit():
            result, message = RomanAlphabet.check_for_romanchars(self.input)
            if not result:
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
        search_result = pattern.search(input)
        grouped = ""
        if search_result:
            grouped = search_result.group()
        # if regex check returns partially or none
        # then means input is incorrect
        if grouped != input:
            result = False, input
        return result

    @staticmethod
    def check_for_binary(input):
        """
            Given number representation has to be decided whether given one
            in binary representation or not.
        """
        result = True
        if not unicode(input).isdigit():
            result = False
        else:
            if filter(lambda x: int(x) > 1, unicode(input)):
                result = False
        return result

    def convert_to_int(self):
        """ To represent roman numeral systemed value with in integer. """
        result = 0
        # Reversed sum has been considered
        # by this way, pre roman char can be considered
        # so current one can be checked whether
        # related value should be added or extracted.
        if not RomanAlphabet.check_for_romansyntax(self.input)[0]:
            return self.input
        pre = 0
        for i in range(len(self.input)-1, -1, -1):
            tmp = BASE_ROMAN_NUMBERS[self.input[i]]
            if tmp < pre:
                result -= tmp
            else:
                result += tmp
            pre = tmp
        return result

    def convert_to_roman(self):
        """ To represent integer value with in roman number system. """
        result = ""
        # To divide given integer input with an
        # order base on roman alphabet,
        # dict must be converted into an ordered list
        base_sorted_numbers = sorted(BASE_ROMAN_NUMBERS.items(),
                                     key=lambda x: x[1], reverse=True)
        try: input = int(self.input)
        except: return self.input
        # Each roman char's integer representation considered,
        # according to the division result returned value generated.
        for rnumber, number in base_sorted_numbers:
            count = input / number
            result += rnumber * count
            input -= count * number
        # To be sure generated representation whether correct or not.
        if not RomanAlphabet.check_for_romansyntax(result):
            raise ConvertionError, 'Error occured while conversion'
        return result

    @staticmethod
    def base_convertion(input, base):
        """
        base represetations as decimal as known, binary or any other between
        2 and 10 can be converted by this method.
        """
        result = ""
        if not unicode(base).isdigit() or base > 10 or base < 2:
            raise InvalidInputError, u"base number must be between 2 and 10."
        tmp = input
        while True:
            result = str(tmp%base) + result
            tmp = tmp / base
            if tmp < base:
                result = str(tmp) + result
                break
        return result

    def convert_to_binary(self):
        """ To represent given input into binary system. """
        result = ""
        # Integer formatted reprentation is more useful, if it is then use it
        # otherwise find out this representation.
        integer_represent = ""
        if str(self.input).isdigit():
            integer_represent = int(self.input)
        else:
            integer_represent = int(self.convert_to_int())

        return RomanAlphabet.base_convertion(integer_represent, 2)

    @staticmethod
    def addition(returned_base="decimal", *args):
        try:
            returned_base = str.lower(returned_base)
            if returned_base not in ['decimal', 'binary', 'roman']:
                raise TypeError
        except TypeError:
            raise InvalidInputError, \
                u"first input must be one of 'decimal', 'binary' or 'roman'"
        # Decimal addition is used for adding one into another
        total = sum(map(lambda x: int(RomanAlphabet(x).convert_to_int()), args))
        result = ""
        # According to the wanted result type convertions are worked
        if returned_base == "decimal":
            result = total
        elif returned_base == "binary":
            result = RomanAlphabet(total).convert_to_binary()
        elif returned_base == "roman":
            result = RomanAlphabet(total).convert_to_roman()
        return result

    @staticmethod
    def multiply(returned_base="decimal", *args):
        try:
            returned_base = str.lower(returned_base)
            if returned_base not in ['decimal', 'binary', 'roman']:
                raise TypeError
        except TypeError:
            raise InvalidInputError, \
                u"first input must be one of 'decimal', 'binary' or 'roman'"
        # Decimal multiplication is used for multipling one into another
        mutiplied = reduce(lambda x,y: int(RomanAlphabet(x).convert_to_int()) *\
                                   int(RomanAlphabet(y).convert_to_int()), \
                                  args, 1)
        result = ""
        # According to the wanted result type convertions are worked
        if returned_base == "decimal":
            result = mutiplied
        elif returned_base == "binary":
            result = RomanAlphabet(mutiplied).convert_to_binary()
        elif returned_base == "roman":
            result = RomanAlphabet(mutiplied).convert_to_roman()
        return result
