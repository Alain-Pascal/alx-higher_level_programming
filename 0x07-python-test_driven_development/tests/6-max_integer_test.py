#!/usr/bin/python3
"""Unittest for max_integer function
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""Define unittest for max_integer()
	"""

	def test_empty_list(self):
		"""Test empty list."""
		self.assertEqual(max_integer([]), None)

	def test_positive_integers(self):
		""" Test a list of positive integers """
		self.assertEqual(max_integer([1, 2, 3, 4]), 4)
		self.assertEqual(max_integer([2, 3, 1, 6]), 6)

	def test_negative_integers(self):
		""" Test a list of negative integers """
		self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
		self.assertEqual(max_integer([-10, -2, -8, -4]), -2)

	def test_mixed_integers(self):
		""" Test a list of mixed
		positive and negative integers
		"""
		self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
		self.assertEqual(max_integer([-10, 5, -2, 8]), 8)

	def test_duplicate_values(self):
		"""Test a list of duplicate values"""
		self.assertEqual(max_integer([1, 2, 2, 4]), 4)
		self.assertEqual(max_integer([3, 2, 4, 4]), 4)

	def test_single_element_list(self):
		"""Test a list with a single element"""
		self.assertEqual(max_integer([5]), 5)
		self.assertEqual(max_integer([-3]), -3)

	def test_large_number(self):
		"""Test a list with large numbers"""
		self.assertEqual(max_integer([5000000, 100000, 4000000]), 5000000)

	def test_floats(self):
		"""Test with float numbers"""
		self.assertEqual(max_integer([1.5, 2.5, 3.4, 5.4]), 5.4)
		self.assertEqual(max_integer([4.5, 2.5, 6.4, 9.2]), 9.2)

	def test_mixed_floats_and_integers(self):
		"""Test with mixed floats and integers"""
		self.assertEqual(max_integer([1.5, 2, 3.4, 4]), 4)
		self.assertEqual(max_integer([3.5, 2, 7.4, 5]), 7.4)
