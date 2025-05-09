#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    def setUp(self):
        """Reset the __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_initialization(self):
        """Test initialization with valid arguments."""
        s = Square(5, 1, 2, 42)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 42)

    def test_auto_id(self):
        """Test auto-incrementing IDs."""
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_invalid_size(self):
        """Test invalid size values."""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(0)

    def test_invalid_x(self):
        """Test invalid x values."""
        with self.assertRaises(TypeError):
            Square(5, "1")
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_invalid_y(self):
        """Test invalid y values."""
        with self.assertRaises(TypeError):
            Square(5, 1, "2")
        with self.assertRaises(ValueError):
            Square(5, 1, -2)

    def test_area(self):
        """Test the area method."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display(self):
        """Test the display method."""
        s = Square(3)
        expected_output = "###\n###\n###\n"
        captured_output = StringIO()
        sys.stdout = captured_output  # redirect stdout
        s.display()
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update_args(self):
        """Test the update method with *args."""
        s = Square(5, 1, 2, 42)
        s.update(89, 7, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        s = Square(5, 1, 2, 42)
        s.update(id=89, size=7, x=3, y=4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s = Square(5, 1, 2, 42)
        expected_dict = {'id': 42, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_str_method(self):
        """Test the __str__ method."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")


if __name__ == "__main__":
    unittest.main()
