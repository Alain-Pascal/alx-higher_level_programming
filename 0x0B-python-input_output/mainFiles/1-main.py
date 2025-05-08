#!/usr/bin/python3
import sys

sys.path.append("../0x0B-python-input_output")
write_file = __import__('1-write_file').write_file

nb_characters = write_file("./files/my_first_file.txt", "This School is "
                           "so cool!\n")

print(nb_characters)
