# Insert src path to account for dual child folder structure.  [Ability to import from src]
import sys
sys.path.insert(1, "C:\\Users\\hlmq\\code\\unit_testing\\src\\")

# unittest is a base module that comes with python
import unittest
import dfcalc

import pandas as pd
from pandas.testing import assert_series_equal


# MUST import unittest.TestCase to inherit asserts
# DOCUMENTATION: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestCalc(unittest.TestCase):

    # Used instead of having repeating data.  Runs BEFORE every test.
    def setUp(self):
        self.df = pd.read_csv("C:\\Users\\hlmq\code\\unit_testing\\test\\df_calc_test_data.csv")
        print('setUp')

    # Used instead of having repeating data.  Runs AFTER every test.
    def tearDown(self):
        del self.df
        print("Tear Down")

    
    def test_add_df_column(self):
        """ Testing Addition"""
        # Check series. Expectation value is a column in the external dataset.  Actual value is computed during the test.
        assert_series_equal(self.df['add expectation'], dfcalc.addDF(self.df), check_names=False)


    def test_subtract_df_column(self):
        """ Testing Subtraction """
        # Check series. Expectation value is a column in the external dataset.  Actual value is computed during the test.
        assert_series_equal(self.df['subtract expectation'], dfcalc.subtractDF(self.df), check_names=False)


    def test_multiply_df_column(self):
        """ Testing Multiplication """
        # Check series. Expectation value is a column in the external dataset.  Actual value is computed during the test.
        assert_series_equal(self.df['multiply expectation'], dfcalc.multiplyDF(self.df), check_names=False)


    def test_divide_df_column(self):
        """ Testing Division """
        # Check series. Expectation value is a column in the external dataset.  Actual value is computed during the test.
        assert_series_equal(self.df['divide expectation'], dfcalc.divideDF(self.df), check_names=False)


# Add this so that you can just run the following command to execute all tests
        # COMMMAND: python test_calc.py
if __name__ == '__main__':
    unittest.main()