#!/usr/bin/python3
import sys

sys.path.append('../0x05-python-exceptions')
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
