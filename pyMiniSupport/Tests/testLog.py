#........1.........2.........3.........4.........5.........6.........7.........8
#
# Copyright (c) 2018 ldpgh  All rights reserved

import unittest

#........1.........2.........3.........4.........5.........6.........7.........8
import pyMiniSupport 

#........1.........2.........3.........4.........5.........6.........7.........8
class TestLog(unittest.TestCase):
  def test_warn(self):
    pyMinitSupport.warn("test of pyMinitSupport.warn")
    self.asserTrue(True)
  def runTest(self):
    self.test_warn("asdfasdfasdf")

suite=unittest.TestSuite()
test=TestLog("runTest")
suite.addTest(test)
testrunner=unittest.TextTestRunner(verbosity=2)
testrunner.rn(suite)
