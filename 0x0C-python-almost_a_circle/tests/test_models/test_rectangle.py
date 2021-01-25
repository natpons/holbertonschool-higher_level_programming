#!/usr/bin/python3
"""
This module contains unittest for /models/rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class TestRectangle defines tests for class Rectangle methods"""

    def test00_args(self):
        """Test for valid arguments"""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 12)

    def test01_int(self):
        """Test valid id attribute"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test02_width_height(self):
        """Test for valid width & height"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)

    def test03_x_y(self):
        """Test for valid x & y"""
        r1 = Rectangle(10, 20)
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test04_none(self):
        """Test with None"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test05_empty(self):
        """Test without arguments"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(e.exception))

    def test06_nan(self):
        """Test with nan"""
        with self.assertRaises(TypeError) as e:
            Rectangle(float('nan'), 2, 3, 4,)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, float('nan'), 3, 4,)
        self.assertEqual('height must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, float('nan'), 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, float('nan'))
        self.assertEqual('y must be an integer', str(e.exception))

    def test07_infinity(self):
        """Test with infinity"""
        with self.assertRaises(TypeError) as e:
            Rectangle(float('inf'), 2, 3, 4,)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, float('inf'), 3, 4,)
        self.assertEqual('height must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, float('inf'), 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, float('inf'))
        self.assertEqual('y must be an integer', str(e.exception))

    def test08_float(self):
        """Test with float"""
        with self.assertRaises(TypeError) as e:
            Rectangle(1.1, 2, 3, 4,)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2.2, 3, 4,)
        self.assertEqual('height must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3.3, 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, 4.4)
        self.assertEqual('y must be an integer', str(e.exception))

    def test09_string(self):
        """Test with string"""
        with self.assertRaises(TypeError) as e:
            Rectangle("1", 2, 3, 4,)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "2", 3, 4,)
        self.assertEqual('height must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, "3", 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, "4")
        self.assertEqual('y must be an integer', str(e.exception))

    def test10_list(self):
        """Test with list"""
        with self.assertRaises(TypeError) as e:
            Rectangle([1, 2, 3], 2, 3, 4)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, [1, 2, 3], 3, 4)
        self.assertEqual('height must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, [1, 2, 3], 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, [1, 2, 3])
        self.assertEqual('y must be an integer', str(e.exception))

    def test11_tuple(self):
        """Test with list"""
        with self.assertRaises(TypeError) as e:
            Rectangle((1, 2, 3), 2, 3, 4)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, (1, 2, 3), 3, 4)
        self.assertEqual('height must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, (1, 2, 3), 4)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, (1, 2, 3))
        self.assertEqual('y must be an integer', str(e.exception))

    def test12_area(self):
        """Test for valid area values"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    if __name__ == '__main__':
        unittest.main()
