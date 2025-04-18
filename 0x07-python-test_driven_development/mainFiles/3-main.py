#!/usr/bin/python3
import sys

sys.path.append("../0x07-python-test_driven_development")

say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Doe")
say_my_name("Walter", "White")
say_my_name("Bob")

try:
    say_my_name(12, "White")
except TypeError as e:
    print(e)
