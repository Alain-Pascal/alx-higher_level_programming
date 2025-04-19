#!/usr/bin/python3
import sys

sys.path.append("../0x07-python-test_driven_development")

max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
