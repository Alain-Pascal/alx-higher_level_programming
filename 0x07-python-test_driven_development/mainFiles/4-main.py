#!/usr/bin/python3
import sys

sys.path.append("../0x07-python-test_driven_development")

print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(1)
print("")
try:
    print_square(-16)
except Exception as e:
    print(e)
print("")
