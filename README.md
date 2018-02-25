# pyMiniSupport
The module contains helper functions needed in my projects.

## Install
pip install git+https://github.com/ldpgh/pyMiniSupport.git

## Short description of the functions
If the package colorama is installed the loggin functions are
  info -> default color
  warn -> yellow
  error -> red
according their meaning.

### Functions for logging
* warn
* error ... does not (yet) stop the program execution
* info
### Functions for progam trace
* prog_line
* prog_file
* prog_file_line

## Use
'
>>> import pyMiniSupport
>>> pyMiniSupport.warn("Falscher Fehler ist falsch.")
WARNING  @  <module>:1   'Falscher Fehler ist falsch.'

>>> from pyMiniSupport import *
>>> error("Falscher Fehler ist falsch.")
WARNING  @  <module>:1   'Falscher Fehler ist falsch.'
'
