#!/usr/bin/python3
import sys

sys.path.append('../0x06-python-classes')
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
