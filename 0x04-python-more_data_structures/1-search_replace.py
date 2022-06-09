#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def replace_element(el):
        return (el if el != search else replace)
    return (list(map(replace_element, my_list)))
