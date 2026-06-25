import unittest
from math_utils import add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):
    """ Test cases for math utility functions. """

    def test_add(self):
        """ Test addition function with positive and negative numbers. """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(0, 0), 0)
        
    def test_subtract(self):
        """ Test subtraction function with positive and negative numbers. """
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_multiply(self):
        """ Test multiplication function with positive and negative numbers. """
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-1, -1), 1)
        
    def test_divide(self):
        """ Test division function with valid inputs. """
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-4, 2), -2)
        self.assertEqual(divide(0, 5), 0)
        
    def test_divide_by_zero(self):
        """ Test division by zero raises ValueError. """
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main() # This will run all tests automatically.