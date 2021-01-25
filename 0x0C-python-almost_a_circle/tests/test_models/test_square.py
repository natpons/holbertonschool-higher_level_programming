#!/usr/bin/python3
"""
This module contains unittest for /models/square.py
"""
import unittest
from models.base import Base
from models.square import Square


class TestRectangle(unittest.TestCase):
    """This class TestRectangle defines tests for class Square methods"""

    def test00_args(self):
        """Test for valid arguments"""
        s1 = Square(5)
        s1.size = 10
