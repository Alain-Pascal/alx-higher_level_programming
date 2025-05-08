#!/usr/bin/python3
"""
12-main
"""
import sys

sys.path.append("../0x0B-python-input_output")
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
