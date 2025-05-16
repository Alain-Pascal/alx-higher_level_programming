#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys
import os
import json


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

    def test_display_with_offset(self):
        """Test the display method with x and y offsets."""
        r = Rectangle(3, 2, 2, 1)
        expected_output = "\n  ###\n  ###\n"
        captured_output = StringIO()
        original_stdout = sys.stdout  # Save the original stdout
        try:
            sys.stdout = captured_output  # Redirect stdout
            r.display()
        finally:
            sys.stdout = original_stdout  # Restore stdout
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

    def test_update_args_over_kwargs(self):
        """Test update method where *args takes precedence over **kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5, id=99, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 89)  # *args takes precedence
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

    def test_create_with_id(self):
        """Test create method with only id."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_with_id_and_width(self):
        """Test create method with id and width."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_create_with_id_width_height(self):
        """Test create method with id, width, and height."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_create_with_all_attributes(self):
        """Test create method with all attributes."""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        # Check if the file exists
        self.assertTrue(os.path.exists("Rectangle.json"))
        # Verify the file content
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_rectangle(self):
        """Test save_to_file with a list of Rectangle objects."""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            saved_data = json.load(file)  # Safely parse JSON file
        self.assertEqual(
            saved_data,
            [{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]
        )

    def test_load_from_file_no_file(self):
        """Test load_from_file when the file does not exist."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_with_data(self):
        """Test load_from_file with valid data."""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        self.assertEqual(rectangles[0].id, 5)
        self.assertEqual(rectangles[0].width, 1)
        self.assertEqual(rectangles[0].height, 2)
        self.assertEqual(rectangles[0].x, 3)
        self.assertEqual(rectangles[0].y, 4)


if __name__ == "__main__":
    unittest.main()
