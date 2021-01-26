#!/usr/bin/python3
"""
This module contains unittest for /models/square.py
"""
import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):
    """This class TestRectangle defines tests for class Square methods"""

    def test_size(self):
        """
        Test initialize the class Square with the size
        """
        test = Square(5)
        self.assertEqual(test.size, 5)

    def test_area(self):
        """
        Test the area function with the square class
        """
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_update(self):
        """
        Test for the update method of the Square class
        """
        s1 = Square(5)
        s1.update(10)
        s1.update(1, 2, 3)
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

    def test_upkwargs(self):
        """
        Test the update with the kwargs
        """
        s1 = Square(5)
        s1.update(x=12)
        s1.update(size=7, y=1)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    if __name__ == '__main__':
        unittest.main()
