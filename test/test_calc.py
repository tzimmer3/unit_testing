# Insert src path to account for dual child folder structure.  [Ability to import from src]
import sys
sys.path.insert(1, "C:\\Users\\hlmq\\code\\unit_testing\\src\\")
# unittest is a base module that comes with python
import unittest
import calc

# MUST import unittest.TestCase to inherit asserts
# DOCUMENTATION: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestCalc(unittest.TestCase):

    # Used instead of having repeating data.  Runs BEFORE every test.
    def setUp(self):
        print('setUp')
        self.case_1_x = 10
        self.case_1_y = 5

        self.case_2_x = -1
        self.case_2_y = 1

        self.case_3_x = -1
        self.case_3_y = -1

    # Used instead of having repeating data.  Runs AFTER every test.
    def tearDown(self):
        pass

    
    def test_add(self):
        # Regular addition
        self.assertEqual(calc.add(self.case_1_x,self.case_1_y),15)
        # One negative number
        self.assertEqual(calc.add(self.case_2_x,self.case_2_y),0)
        # Two negative numbers
        self.assertEqual(calc.add(self.case_3_x,self.case_3_y),-2)


    def test_subtract(self):
        # Regular subtraction
        self.assertEqual(calc.subtract(10,5),5)
        # One negative number
        self.assertEqual(calc.subtract(-1,1),-2)
        # Two negative numbers
        self.assertEqual(calc.subtract(-1,-1),0)


    def test_multiply(self):
        # Regular multiplication
        self.assertEqual(calc.multiply(10,5),50)
        # One negative number
        self.assertEqual(calc.multiply(-1,1),-1)
        # Two negative numbers
        self.assertEqual(calc.multiply(-1,-1),1)


    def test_divide(self):
        # Regular division
        self.assertEqual(calc.divide(10,5),2)
        # One negative number
        self.assertEqual(calc.divide(-1,1),-1)
        # Two negative numbers
        self.assertEqual(calc.divide(-1,-1),1)
        # Decimals
        self.assertEqual(calc.divide(5,2),2.5)
        # Divide by 0
        # HANDLES the ValueError in the function using a context manager
        with self.assertRaises(ValueError):
            calc.divide(10,0)



# Add this so that you can just run the following command to execute all tests
        # COMMMAND: python test_calc.py
if __name__ == '__main__':
    unittest.main()