import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
my_list = ['hello', 'world']

lib.print_python_list_info(my_list)
del my_list[1]
lib.print_python_list_info(my_list)

my_list = my_list + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]

lib.print_python_list_info(my_list)
my_list = []
lib.print_python_list_info(my_list)
my_list.append(0)
lib.print_python_list_info(my_list)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
lib.print_python_list_info(my_list)
my_list.pop()
lib.print_python_list_info(my_list)
