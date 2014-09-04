RomanNumbers
============
[![Build Status](https://travis-ci.org/RedXBeard/RomanNumbers.svg?branch=master)](https://travis-ci.org/RedXBeard/RomanNumbers)

Roman or Integer numbers can be converted into eachother an additionally representation of each one of them into binary
format.

Installation
------------

```bash
$ pip install RomanAlphabet
```

Usage
-----
To represent an integer value into roman numeral system;

```ipython
: from romanalphabet.romanalphabet import RomanAlphabet
: rr = RomanAlphabet("4785")
: rr.convert_to_roman()
: 'MMMMDCCLXXXV'
```

or into binary;

```ipython
...
: rr.convert_to_binary()
: '1001010110001'
```

Also roman numbers can be an input and represented with integer and binary format. If anything will goes wrong then for input as an example, none roman numerics if given then an understandable error will displayed.

```ipython
: rr = RomanAlphabet("CVII")
: rr.convert_to_int()
: 107
: rr.convert_to_binary()
: 1101011
: rr = RomanAlphabet("MXXCVII")
---------------------------------------------------------------------------
InvalidInputError                         Traceback (most recent call last)
<ipython-input-4-928ae041fe2c> in <module>()
----> 1 rr = RomanAlphabet("MXXCVII")

/Users/barbaros/.virtualenvs/RomanAlphabet/project/RomanNumbers/romanalphabet/romanalphabet.py in __init__(self, input)
     21             if not result:
     22                 raise InvalidInputError, \
---> 23                         "Input has unqualified chars; '%s'" % message
     24
     25     @staticmethod

InvalidInputError: Input has unqualified chars; 'MXXCVII'
: rr = RomanAlphabet("CTII")
---------------------------------------------------------------------------
InvalidInputError                         Traceback (most recent call last)
<ipython-input-5-9cb900ee7522> in <module>()
----> 1 rr = RomanAlphabet("TVII")

/Users/barbaros/.virtualenvs/RomanAlphabet/project/RomanNumbers/romanalphabet/romanalphabet.py in __init__(self, input)
     21             if not result:
     22                 raise InvalidInputError, \
---> 23                         "Input has unqualified chars; '%s'" % message
     24
     25     @staticmethod

InvalidInputError: Input has unqualified chars; 'T'
```
