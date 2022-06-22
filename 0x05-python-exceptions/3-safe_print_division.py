#!/usr/bin/python3

def safe_print_division(a, b):
    """Devides 2 integers and prints the result

    Args:
        a (int): integer 1
        b (int): integer 2

    Returns:
        the quotient
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return ("{}".format(result))
