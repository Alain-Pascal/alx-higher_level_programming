#!/usr/bin/python3
import sys

sys.path.append("../0x0A-python-inheritance")

BaseGeometry = __import__("6-base_geometry").BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
