RomanNumbers
============

.. image:: https://travis-ci.org/RedXBeard/RomanNumbers.svg?branch=master
    :target: https://travis-ci.org/RedXBeard/RomanNumbers 
    :alt: Build
.. image:: https://pypip.in/download/RomanAlphabet/badge.svg
    :target: https://pypi.python.org/pypi//RomanAlphabet/
    :alt: Downloads
.. image:: https://pypip.in/version/RomanAlphabet/badge.svg
    :target: https://pypi.python.org/pypi/RomanAlphabet/
    :alt: Latest Version
.. image:: https://pypip.in/py_versions/RomanAlphabet/badge.svg
    :target: https://pypi.python.org/pypi/RomanAlphabet/
    :alt: Supported Python versions
.. image:: https://pypip.in/license/RomanAlphabet/badge.svg
    :target: https://pypi.python.org/pypi/RomanAlphabet/
    :alt: License
    
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
    : rr.to_roman()
    : 'MMMMDCCLXXXV'

or into binary;

.. code-block:: python
    
    ...
    : rr.to_binary()
    : '1001010110001'


numbers can also be added or mutiplied into one another, as following; result could be three type of numeric format; "decimal", "binary" or in "roman";

.. code-block:: python
    
    : RomanAlphabet.operations.add(1).to_roman()
    : 'I'
    : RomanAlphabet.operations.multiply(1,2,3).to_roman()
    : 'VI'
    : RomanAlphabet.operations.multiply(1,2,3).to_decimal()
    : 6
    : RomanAlphabet.operations.add(1,2,3).to_binary()
    : '110'
    : RomanAlphabet.operations.multiply(7,4,2,4,2,3).to_decimal()
    : 1344
    : RomanAlphabet.operations.multiply(7,4,2,4,2,3).to_binary()
    : '10101000000'
