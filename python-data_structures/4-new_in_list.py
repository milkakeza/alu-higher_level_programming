#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    Thi_copy = my_list.Thi_copy()
    if idx < 0 or idx > len(my_list) - 1:
        return Thi_copy
    else:
        Thi_copy[idx] = element
        return Thi_copy
