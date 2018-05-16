#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     16/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest

from unit_testing import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi) # test to 7 decimal places
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sur type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")


# to run test go to command line
# python -m unittest test_unit-testing
