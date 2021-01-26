#!/usr/bin/python3
"""
This module contains unittest for /models/rectangle.py
"""
import unittest
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

        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle(None)

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

    def test09_string1(self):
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

    def test09_string2(self):
        """Test the str method"""
        r1 = Rectangle(2, 2, 1, 1, 15)
        self.assertEqual(str(r1), "[Rectangle] (15) 1/1 - 2/2")

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

    def test13_without_xy(self):
        """ Test without x and y"""
        r4 = Rectangle(10, 20)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

    def test14_x(self):
        """ Test with x"""
        r5 = Rectangle(10, 20, 5)
        self.assertEqual(r5.x, 5)

    def test15_y(self):
        """ Test with y"""
        r6 = Rectangle(10, 20, 5, 6)
        self.assertEqual(r6.y, 6)

    def test16_init_all_param(self):
        """ Test initialize tha class with all parameters"""
        r7 = Rectangle(10, 20, 5, 6, 4)
        self.assertEqual(r7.width, 10)
        self.assertEqual(r7.height, 20)
        self.assertEqual(r7.x, 5)
        self.assertEqual(r7.y, 6)
        self.assertEqual(r7.id, 4)

    def test17_type(self):
        """Test if it is not a integer"""
        with self.assertRaises(TypeError):
            Rectangle(5, "coucou")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, [8])
        with self.assertRaises(TypeError):
            Rectangle(10, 3, 1.4, 1)
        with self.assertRaises(TypeError):
            Rectangle(True, 3, 6, 1)

    def test18_negative(self):
        """Test with negative number"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 4, -9)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -4, 9)
        with self.assertRaises(ValueError):
            Rectangle(10, -20, 4, 9)

    def test_update(self):
        """
        Test for the uptade method
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_up_kwargs(self):
        """ Test for kwargs """
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(height=1)
        r2.update(width=1, x=2)
        r2.update(y=1, width=2, x=3, id=90)
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r2), "[Rectangle] (90) 1/3 - 4/2")

    if __name__ == '__main__':
        unittest.main()
