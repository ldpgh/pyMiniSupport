# pyMiniSupport
The module contains helper functions needed in my projects.

## Install
pip install git+https://github.com/ldpgh/pyMiniSupport.git

## Short description of the functions
If the package colorama is installed the loggin functions are
- info -> default color (bright)
- warn -> yellow
- error -> red

according their meaning.

### Functions for logging
* info
* warn
* error ... does not (yet) stop the program execution
### Functions for progam trace
* prog_line
* prog_file
* prog_file_line

## Use case ... see simple test run
```pyMiniSupport>>
pyMiniSupport>>python -c "import pyMiniSupport.Tests.testLog"

runTest (pyMiniSupport.Tests.testLog.TestLog) ...
INFO  @  runTest:14   'test of pyMiniSupport.info'

WARNING  @  runTest:15   'test of pyMiniSupport.warn'

ERROR  @  runTest:16   'test of pyMiniSupport.error'

17

runTest

runTest:19
ok

----------------------------------------------------------------------
Ran 1 test in 0.047s

OK

pyMiniSupport>>
```
