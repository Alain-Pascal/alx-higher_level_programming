#!/usr/bin/python3
import sys

sys.path.append("../0x08-python-more_classes")
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(
    my_rectangle.area(), my_rectangle.perimeter()
    ))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(
    my_rectangle.area(), my_rectangle.perimeter())
)
