#!/usr/bin/python3
import sys

sys.path.append("../0x09-python-everything_is_object")

magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())
