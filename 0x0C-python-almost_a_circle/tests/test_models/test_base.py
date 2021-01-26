#!/usr/bin/python3
"""
This module contains unittest for /models/base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This class TestBase defines tests for class Base methods"""

    def test00_int(self):
        """Test validation id attribute"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-5)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -5)

    def test01_none(self):
        """Test None id input"""
        b6 = Base(None)
        self.assertEqual(b6.id, 4)

    def test02_float(self):
        """Test float input"""
        b7 = Base(2.4)
        self.assertEqual(b7.id, 2.4)

    def test03_string(self):
        """Test string input"""
        b8 = Base("Barcelonnette/*")
        self.assertEqual(b8.id, "Barcelonnette/*")

    def test04_list(self):
        """Test list input"""
        b9 = Base([1, 2, 3])
        self.assertEqual(b9.id, [1, 2, 3])

    def test05_tuple(self):
        """Test tuple input"""
        b10 = Base((10, 20, 30))
        self.assertEqual(b10.id, (10, 20, 30))

    if __name__ == '__main__':
        unittest.main()
