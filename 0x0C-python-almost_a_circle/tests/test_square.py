#!/usr/bin/python3
import json
import os
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

    def test_display_with_offset(self):
        """Test the display method with x and y offsets."""
        s = Square(3, 2, 1)
        expected_output = "\n  ###\n  ###\n  ###\n"
        captured_output = StringIO()
        original_stdout = sys.stdout  # Save the original stdout
        try:
            sys.stdout = captured_output  # Redirect stdout
            s.display()
        finally:
            sys.stdout = original_stdout  # Restore stdout
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Square.save_to_file(None)
        # Check if the file exists
        self.assertTrue(os.path.exists("Square.json"))
        # Verify the file content
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_square(self):
        """Test save_to_file with a list of Square objects."""
        s = Square(5, 1, 2, 42)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            saved_data = json.load(file)  # Safely parse JSON file
        self.assertEqual(
            saved_data,
            [{"id": 42, "size": 5, "x": 1, "y": 2}]
        )

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

    def test_load_from_file_no_file(self):
        """Test load_from_file when the file does not exist."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_with_data(self):
        """Test load_from_file with valid data."""
        s = Square(5, 1, 2, 42)
        Square.save_to_file([s])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0].id, 42)
        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[0].x, 1)
        self.assertEqual(squares[0].y, 2)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s = Square(5, 1, 2, 42)
        expected_dict = {'id': 42, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_str_method(self):
        """Test the __str__ method."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_create_with_id(self):
        """Test create method with only id."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_with_id_and_size(self):
        """Test create method with id and size."""
        s = Square.create(**{'id': 89, 'size': 5})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)

    def test_create_with_id_size_and_x(self):
        """Test create method with id, size, and x."""
        s = Square.create(**{'id': 89, 'size': 5, 'x': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 3)

    def test_create_with_all_attributes(self):
        """Test create method with all attributes."""
        s = Square.create(**{'id': 89, 'size': 5, 'x': 3, 'y': 4})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)


if __name__ == "__main__":
    unittest.main()
