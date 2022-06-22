#!/usr/bin/python3
import sys

sys.path.append('../0x05-python-exceptions')
safe_print_list_int = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_int(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_int(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_int(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
