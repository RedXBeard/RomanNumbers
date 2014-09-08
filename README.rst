RomanNumbers
============
.. image:: https://travis-ci.org/RedXBeard/RomanNumbers.svg?branch=master
    :target: https://travis-ci.org/RedXBeard/RomanNumbers

Roman or Integer numbers can be converted into eachother an additionally representation of each one of them into binary
format.

Installation
------------

.. code-block:: bash
    $ pip install RomanAlphabet


Usage
-----
To represent an integer value into roman numeral system;

.. code-block:: python
    : from romanalphabet.romanalphabet import RomanAlphabet
    : rr = RomanAlphabet("4785")
    : rr.convert_to_roman()
    : 'MMMMDCCLXXXV'

or into binary;

.. code-block:: python
    ...
    : rr.convert_to_binary()
    : '1001010110001'


numbers can also be added or mutiplied into one another, as following; result could be three type of numeric format; "decimal", "binary" or in "roman";

.. code-block:: python
    : RomanAlphabet.addition("roman",1)
    : 'I'
    : RomanAlphabet.multiply("roman",1,2,3)
    : 'VI'
    : RomanAlphabet.multiply("decimal",1,2,3)
    : 6
    : RomanAlphabet.addition("binary",1,2,3)
    : '110'
    : RomanAlphabet.multiply("decimal",7,4,2,4,2,3)
    : '10101000000'


If first argument not one of <code>decimal</code> <code>roman</code> <code>binary</code> then the following error will be displayed

.. code-block:: python
    : RomanAlphabet.multiply("deciaml",7,4,2,4,2,3)
    ---------------------------------------------------------------------------
    InvalidInputError                         Traceback (most recent call last)
    <ipython-input-6-bbd7bcac2f3a> in <module>()
    ----> 1 RomanAlphabet.multiply("deciaml",7,4,2,4,2,3)

    /Users/denizci/.virtualenvs/RomanAlphabet/project/RomanNumbers/romanalphabet/romanalphabet.py in multiply(returned_base, *args)
        172         except TypeError:
        173             raise InvalidInputError, \
    --> 174                 u"first input must be one of 'decimal', 'binary' or 'roman'"
        175         # Decimal multiplication is used for multipling one into another
        176         mutiplied = reduce(lambda x,y: int(RomanAlphabet(x).convert_to_int()) *\

    InvalidInputError: first input must be one of 'decimal', 'binary' or 'roman'


Also roman numbers can be an input and represented with integer and binary format. If anything will goes wrong then for input as an example, none roman numerics if given then an understandable error will displayed.

.. code-block:: python
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
