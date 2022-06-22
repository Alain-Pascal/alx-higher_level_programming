#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely

    Args:
        fct: pointer to a function
        args: arguments passed

    Returns:
        result of the function, otherwise None
    """
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    else:
        return (result)
