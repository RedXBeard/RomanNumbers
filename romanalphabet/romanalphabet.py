# -*- coding: utf-8 -*-
import re


def convert_result(base, result):
    mapper = {
        "decimal": lambda x: x,
        "binary": lambda x: RomanAlphabet(x).to_binary(),
        "roman": lambda x: RomanAlphabet(x).to_roman()
    }
    return mapper[base](result)


class InvalidinptError(Exception): pass


class ConvertionError(Exception): pass


BASE_ROMAN_NUMBERS = dict(M=1000, CM=900, D=500, CD=400, C=100, XC=90,
                          L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1)


class Operations:
    def __init__(self):
        self.result = None

    def add(self, *args):
        def _add():
            total = sum(map(lambda x: int(RomanAlphabet(x).to_int()), args))
            self.result = total
            return self

        return _add()

    def subtruct(self, *args):
        def _subtruct():
            try:
                num = int(RomanAlphabet(args[0]).to_int())
            except IndexError:
                raise InvalidinptError

            for arg in args[1:]:
                num -= int(RomanAlphabet(arg).to_int())
            self.result = num
            return self

        return _subtruct()

    def multiply(self, *args):
        def _multiply():
            multiplied = 1
            for arg in args:
                multiplied *= arg
            self.result = multiplied
            return self

        return _multiply()

    def division(self, *args):
        def _division():
            try:
                num = int(RomanAlphabet(args[0]).to_int())
            except IndexError:
                raise InvalidinptError

            for arg in args[1:]:
                num /= int(RomanAlphabet(arg).to_int())
            self.result = num
            return self

        return _division()

    def to_decimal(self):
        return convert_result("decimal", self.result)

    def to_binary(self):
        return convert_result("binary", self.result)

    def to_roman(self):
        return convert_result("roman", self.result)


class RomanAlphabet(object):
    operations = Operations()

    def __init__(self, inpt):
        self.inpt = str(inpt).upper()
        # If inpt is an integer ...
        if not str(self.inpt).isdigit():
            result, message = RomanAlphabet.check_for_romanchars(self.inpt)
            if not result:
                raise InvalidinptError

    @staticmethod
    def check_for_romanchars(inpt):
        """ To check alphabet and give exact unmatched ones. """
        # chars has to be checked
        # if there is any unknown one according to the alphabet
        # defined globally.
        acceptable_chars = BASE_ROMAN_NUMBERS.keys()
        unknown_chars = list(filter(lambda x: x not in acceptable_chars, inpt))
        # If there is any one, class initialization has to stop.
        # if not checking process should be c[ontinued with syntactically.
        if unknown_chars:
            result = False, ", ".join(unknown_chars)
        else:
            result = RomanAlphabet.check_for_romansyntax(inpt)
        return result

    @staticmethod
    def check_for_romansyntax(inpt):
        """ syntactically check if given number for roman numeral system. """
        result = True, ""
        # Regex used to check syntactically of given string
        pattern = re.compile("""M*(CM|CD|D?C{0,3})
                                (XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$""",
                             re.VERBOSE)
        search_result = pattern.search(inpt)
        grouped = ""
        if search_result:
            grouped = search_result.group()
        # if regex check returns partially or none
        # then means inpt is incorrect
        if grouped != inpt:
            result = False, inpt
        return result

    @staticmethod
    def check_for_binary(inpt):
        """
            Given number representation has to be decided whether given one
            in binary representation or not.
        """
        result = True
        if not inpt.isdigit():
            result = False
        else:
            if list(filter(lambda x: int(x) > 1, inpt)):
                result = False
        return result

    def to_int(self):
        """ To represent roman numeral systemed value with in integer. """
        result = 0
        # Reversed sum has been considered
        # by this way, pre roman char can be considered
        # so current one can be checked whether
        # related value should be added or extracted.
        if not RomanAlphabet.check_for_romansyntax(self.inpt)[0]:
            return self.inpt
        pre = 0
        for i in range(len(self.inpt) - 1, -1, -1):
            tmp = BASE_ROMAN_NUMBERS[self.inpt[i]]
            if tmp < pre:
                result -= tmp
            else:
                result += tmp
            pre = tmp
        return result

    def to_roman(self):
        """ To represent integer value with in roman number system. """
        result = ""
        # To divide given integer inpt with an
        # order base on roman alphabet,
        # dict must be converted into an ordered list
        base_sorted_numbers = sorted(BASE_ROMAN_NUMBERS.items(),
                                     key=lambda x: x[1], reverse=True)
        try:
            inpt = int(self.inpt)
        except (ValueError, TypeError):
            return self.inpt
        # Each roman char's integer representation considered,
        # according to the division result returned value generated.
        for rnumber, number in base_sorted_numbers:
            count = int(inpt / number)
            result += rnumber * count
            inpt -= count * number
        # To be sure generated representation whether correct or not.
        if not RomanAlphabet.check_for_romansyntax(result):
            raise ConvertionError
        return result

    @staticmethod
    def base_convertion(inpt, base):
        """
        base represetations as decimal as known, binary or any other between
        2 and 10 can be converted by this method.
        """
        result = ""
        if not str(base).isdigit() or base > 10 or base < 2:
            raise InvalidinptError
        tmp = inpt
        while True:
            result = str(tmp % base) + result
            tmp = tmp // base
            if tmp < base:
                result = str(tmp) + result
                break
        return result

    def to_binary(self):
        """ To represent given inpt into binary system. """
        # Integer formatted reprentation is more useful, if it is then use it
        # otherwise find out this representation.
        if str(self.inpt).isdigit():
            integer_represent = int(self.inpt)
        else:
            integer_represent = int(self.to_int())

        return RomanAlphabet.base_convertion(integer_represent, 2)
