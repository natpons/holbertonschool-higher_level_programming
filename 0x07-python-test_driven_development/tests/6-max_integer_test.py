#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer function"""

    def test_max_integer(self):
        """Test for max integer"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1.5, 2, 3.8, 1.4]), 3.8)
        self.assertEqual(max_integer([34, 5, 34, 19, 0, 33, 34]), 34)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, -float('inf')]), 2)
        self.assertRaises(TypeError, max_integer, [1, 2, 'a', 4])
        self.assertRaises(TypeError, max_integer, [1, "free", 3, 4])
        self.assertRaises(TypeError, max_integer, 123)
        self.assertEqual(max_integer(["Hello", "Hi", "Good Morning"]), "Hi")
        self.assertEqual(max_integer([1 - 3, 2 * 3, 7 + 3]), 10)

if __name__ == '__main__':
    unittest.main()
