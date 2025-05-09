#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset the __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test auto-incrementing IDs."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test custom ID assignment."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_mixed_ids(self):
        """Test a mix of auto and custom IDs."""
        b1 = Base()
        b2 = Base(42)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 42)
        self.assertEqual(b3.id, 2)

    def test_id_with_negative(self):
        """Test custom ID with a negative value."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_with_zero(self):
        """Test custom ID with zero."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_with_large_number(self):
        """Test custom ID with a large number."""
        b = Base(999999999999)
        self.assertEqual(b.id, 999999999999)

    def test_id_with_string(self):
        """Test custom ID with a string."""
        b = Base("string_id")
        self.assertEqual(b.id, "string_id")

    def test_id_with_float(self):
        """Test custom ID with a float."""
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

    def test_id_with_none(self):
        """Test ID when None is passed explicitly."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_private_nb_objects(self):
        """
        Test that __nb_objects is private and cannot be accessed directly.
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_nb_objects_increment(self):
        """Test that __nb_objects increments correctly."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_multiple_instances(self):
        """Test multiple instances with mixed IDs."""
        b1 = Base()
        b2 = Base(100)
        b3 = Base()
        b4 = Base(-50)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, -50)
        self.assertEqual(b5.id, 3)


if __name__ == "__main__":
    unittest.main()
