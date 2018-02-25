#........1.........2.........3.........4.........5.........6.........7.........8
#
# Copyright (c) 2018 ldpgh  All rights reserved

import unittest

#........1.........2.........3.........4.........5.........6.........7.........8
import pyMiniSupport 
import pyMiniSupport.Log
class TestLog(unittest.TestCase):
  def runTest(self):
    print(""); pyMiniSupport.Log.info("test of pyMiniSupport.Log.info()")
    print(""); pyMiniSupport.Log.warn("test of pyMiniSupport.Log.warn()")
    print(""); pyMiniSupport.Log.error("test of pyMiniSupport.Log.error()")
    print(""); print(pyMiniSupport.Log.prog_line())
    print(""); print(pyMiniSupport.Log.prog_file())
    print(""); print(pyMiniSupport.Log.prog_file_line())

#........1.........2.........3.........4.........5.........6.........7.........8
from pyMiniSupport.Log import *
class TestLogShort(unittest.TestCase):
  def runTest(self):
    print(""); info("test of info()")
    print(""); warn("test of warn()")
    print(""); error("test of error()")
    print(""); print(prog_line())
    print(""); print(prog_file())
    print(""); print(prog_file_line())

suite=unittest.TestSuite()
suite.addTest(TestLog("runTest"))
suite.addTest(TestLogShort("runTest"))
unittest.TextTestRunner(verbosity=2).run(suite)
