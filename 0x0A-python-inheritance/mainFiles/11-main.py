#!/usr/bin/python3
import sys

sys.path.append("../0x0A-python-inheritance")

Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
