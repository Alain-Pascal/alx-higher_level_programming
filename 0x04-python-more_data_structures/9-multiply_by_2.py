#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dict = {}
    for dict in a_dictionary:
        mul_dict[dict] = a_dictionary[dict] * 2
    return (mul_dict)
