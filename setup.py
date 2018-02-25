#........1.........2.........3.........4.........5.........6.........7.........8
#
# Copyright (c) 2018 ldpgh  All rights reserved

from setuptools import setup
import sys

sys.dont_write_bytecode=True

setup(
   name='pyMiniSupport',
   version='1.0.5',
   description='The module contains helper functions needed in my projects.',
   author='ldpgh',
   packages=['pyMiniSupport'],
   test_suite="pyMiniSupport.Tests.testLog"
)
