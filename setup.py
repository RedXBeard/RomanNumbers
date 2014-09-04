#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()

setup(
  name = 'RomanAlphabet',
  packages = ['RomanAlphabet'],
  version = '0.3',
  description = 'Numeral systems, binary, roman, integer',
  author = u'Barbaros YILDIRIM',
  author_email = 'barbarosaliyildirim@gmail.com',
  url = 'https://github.com/RedXBeard/RomanNumbers',
  download_url = 'https://github.com/RedXBeard/RomanNumbers/tarball/0.3',
  keywords = ['roman', 'romanalphabet', 'integer converter', 'integer to roman',
              'roman to integer', 'binary', 'binary convertion'],
  classifiers = [
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Natural Language :: English',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
  ],
  long_description = long_description
)
