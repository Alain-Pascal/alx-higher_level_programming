#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list
    Args:
        my_list (list): list from where to print elements
        x (int): number of elements of my_list to print
    Returns:
        the number of elements printed
    """
    elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements += 1
        except IndexError:
            break

    print("")
    return (elements)
