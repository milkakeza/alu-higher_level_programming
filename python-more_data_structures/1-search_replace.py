#!/usr/bin/python3


def search_replace(my_list, search, replace):

    NewList = []
    for element in my_list:
        if element == search:
            NewList.append(replace)
        else:
            NewList.append(element)
    return NewList
