#!/usr/bin/python3
import sys

sys.path.append("../0x09-python-everything_is_object")

copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(my_list == new_list)
print(my_list is new_list)
