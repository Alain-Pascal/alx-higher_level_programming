#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers
    Args:
        my_list (list): list from where to print elements
        x (int): number of elements of my_list to print
    Returns:
        the real number of elements printed
    """
    el = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            el += 1
        except (ValueError, TypeError):
            continue

    print("")
    return (el)
