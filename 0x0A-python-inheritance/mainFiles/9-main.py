#!/usr/bin/python3
import sys

sys.path.append("../0x0A-python-inheritance")

Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
