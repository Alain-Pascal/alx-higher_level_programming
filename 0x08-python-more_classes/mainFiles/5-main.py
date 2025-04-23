#!/usr/bin/python3
import sys

sys.path.append("../0x08-python-more_classes")
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)

print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
