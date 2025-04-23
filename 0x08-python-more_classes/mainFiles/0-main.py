#!/usr/bin/python3
import sys

sys.path.append("../0x08-python-more_classes")

Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()

print(type(my_rectangle))
print(my_rectangle.__dict__)
