#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Reset the __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_initialization(self):
        """Test initialization with valid arguments."""
        r = Rectangle(10, 2, 1, 1, 42)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 42)

    def test_auto_id(self):
        """Test auto-incrementing IDs."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(5, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_invalid_width(self):
        """Test invalid width values."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_invalid_height(self):
        """Test invalid height values."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_invalid_x(self):
        """Test invalid x values."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1", 1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 1)

    def test_invalid_y(self):
        """Test invalid y values."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "1")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -1)

    def test_area(self):
        """Test the area method."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        """Test the display method."""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        captured_output = StringIO()
        sys.stdout = captured_output  # redirect stdout
        r.display()
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update_args(self):
        """Test the update method with *args."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_str_method(self):
        """Test the __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
