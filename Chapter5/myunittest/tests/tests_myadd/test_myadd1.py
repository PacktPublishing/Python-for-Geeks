#test_myadd1.py test suite for myadd function
import unittest
from myunittest.src.myadd.myadd import add

class MyAddTestSuite(unittest.TestCase):

    def test_add1(self):
        """ test case to validate two positive numbers"""
        self.assertEqual(15, add(10 , 5), "should be 15")

    def test_add2(self):
        """ test case to validate positive and negative numbers"""
        self.assertEqual(5, add(10 , -5), "should be 5")

    def test_add3(self):
        """ test case to validate positive and negative numbers"""
        self.assertEqual(-5, add(-10 , 5), "should be -5")

    def test_add4(self):
        """ test case to validate two negative numbers"""
        self.assertEqual(-15, add(-10 , -5), "should be -15")

if __name__ == '__main__':
    unittest.main()
