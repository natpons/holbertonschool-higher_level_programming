#!/usr/bin/python3
"""
This module contains unittest for /models/square.py
"""
import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):
    """This class TestRectangle defines tests for class Square methods"""

    def test00_size(self):
        """
        Test initialize the class Square with the size
        """
        s0 = Square(5)
        self.assertEqual(s0.size, 5)

    def test01_area(self):
        """
        Test the area function with the square class
        """
        s1 = Square(2)
        s2 = Square(3, 1)
        s3 = Square(4, 1, 3)
        self.assertEqual(s1.area(), 4)
        self.assertEqual(s2.area(), 9)
        self.assertEqual(s3.area(), 16)

    def test02_update(self):
        """
        Test for the update method of the Square class
        """
        s1 = Square(5)
        s1.update(10)
        s1.update(1, 2, 3)
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

    def test03_upkwargs(self):
        """
        Test the update with the kwargs
        """
        s1 = Square(5)
        s1.update(x=12)
        s1.update(size=7, y=1)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test04_args(self):
        """Test for valid arguments"""
        s = Square(10, 2, 3, 12)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 12)

    def test05_excess_args(self):
        """Test for excess arguments"""
        with self.assertRaises(TypeError) as e:
            s = Square(10, 2, 3, 12, 5, 8)
        self.assertEqual(
            "__init__() takes from 2 to 5 positional" +
            " arguments but 7 were given",
            str(e.exception))

        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(None)

    def test06_empty(self):
        """Test without arguments"""
        with self.assertRaises(TypeError) as e:
            s = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(e.exception))

    def test07_nan(self):
        """Test with nan"""
        with self.assertRaises(TypeError) as e:
            Square(float('nan'), 2, 3, 4)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, float('nan'), 3, 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, 2, float('nan'), 4)
        self.assertEqual('y must be an integer', str(e.exception))

    def test08_infinity(self):
        """Test with infinity"""
        with self.assertRaises(TypeError) as e:
            Square(float('inf'), 2, 3, 4,)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, float('inf'), 3, 4,)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, 2, float('inf'), 4)
        self.assertEqual('y must be an integer', str(e.exception))

    def test09_float(self):
        """Test with float"""
        with self.assertRaises(TypeError) as e:
            Square(1.1, 2, 3, 4,)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, 2.2, 3, 4,)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, 2, 3.3, 4)
        self.assertEqual('y must be an integer', str(e.exception))

    def test10_string(self):
        """Test with string"""
        with self.assertRaises(TypeError) as e:
            Square("1", 2, 3, 4)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, "2", 3, 4,)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, 2, "3", 4)
        self.assertEqual('y must be an integer', str(e.exception))

    def test11_list(self):
        """Test with list"""
        with self.assertRaises(TypeError) as e:
            Square([1, 2, 3], 2, 3, 4)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, [1, 2, 3], 3, 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, 2, [1, 2, 3], 4)
        self.assertEqual('y must be an integer', str(e.exception))

    def test12_tuple(self):
        """Test with list"""
        with self.assertRaises(TypeError) as e:
            Square((1, 2, 3), 2, 3, 4)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, (1, 2, 3), 3, 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(1, 2, (1, 2, 3), 4)
        self.assertEqual('y must be an integer', str(e.exception))

    def test13_type(self):
        """Test with boolean"""
        with self.assertRaises(TypeError):
            Square(True, 3, 6, 1)

    def test14_negative(self):
        """Test with negative number"""
        with self.assertRaises(ValueError):
            Square(-10, 20)
        with self.assertRaises(ValueError):
            Square(10, -20, 4, 9)
        with self.assertRaises(ValueError):
            Square(10, 20, -4, 9)

    if __name__ == '__main__':
        unittest.main()
