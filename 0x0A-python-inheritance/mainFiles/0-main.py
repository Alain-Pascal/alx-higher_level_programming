#!/usr/bin/python3
import sys

sys.path.append("../0x0A-python-inheritance")

lookup = __import__("0-lookup").lookup


class MyClass1(object):
    """MyClass1"""
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        """My method"""
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
