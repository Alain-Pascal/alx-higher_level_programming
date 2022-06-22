#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with "{:d}".format()
    Args:
        value (int): the value to print
    Returns:
        True if value has been correctly printed, False otherwise
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return (False)
    else:
        return (True)
