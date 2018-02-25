#........1.........2.........3.........4.........5.........6.........7.........8
#
# Copyright (c) 2018 ldpgh  All rights reserved

from unittest import TestCase

#........1.........2.........3.........4.........5.........6.........7.........8
import pyMiniSupport 

#........1.........2.........3.........4.........5.........6.........7.........8
class TestLog(TestCase):
  def test_warn(self):
    pyMinitSupport.warn("test of pyMinitSupport.warn")
    self.asserTrue(True)
  def runTest(self):
    self.test_war()

TestSuite()
