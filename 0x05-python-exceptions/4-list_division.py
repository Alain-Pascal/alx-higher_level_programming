#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists

    Args:
        my_list_1 (list): first list containing any type
        my_list_2 (list): second list containing any type
        list_length: length of list

    Returns:
        a new list (length = list_length) with all divisions
    """
    new_list = []
    for i in range(0, list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new_list.append(quotient)

    return (new_list)
