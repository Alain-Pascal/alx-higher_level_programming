#!/usr/bin/python3
import sys

sys.path.append("../0x0B-python-input_output")
append_after = __import__('100-append_after').append_after

append_after("./files/append_after_100.txt", "Python", "\"C is fun!\"\n")
