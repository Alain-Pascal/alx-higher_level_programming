#!/usr/bin/python3
import sys

sys.path.append("../0x0A-python-inheritance")
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
