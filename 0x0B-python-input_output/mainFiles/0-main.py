#!/usr/bin/python3
import sys

sys.path.append("../0x0B-python-input_output")
read_file = __import__('0-read_file').read_file

read_file("./files/my_file_0.txt")
