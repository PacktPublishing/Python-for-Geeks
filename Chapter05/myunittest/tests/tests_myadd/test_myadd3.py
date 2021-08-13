#test_myadd3.py test suite for myadd2 class method to validate errors
import unittest
from myunittest.src.myadd.myadd2 import MyAdd

class MyAddTestSuite(unittest.TestCase):
    def setUp(self):
        self.myadd = MyAdd()

    def test_typeerror1(self):
        """ test case to check if we can handle non number input"""
        self.assertRaises(TypeError, self.myadd.add, 'a' , -5)

    def test_typeerror2(self):
        """ test case to check if we can handle non number input"""
        self.assertRaises(TypeError, self.myadd.add, 'a' , 'b')

if __name__ == '__main__':
    unittest.main()

