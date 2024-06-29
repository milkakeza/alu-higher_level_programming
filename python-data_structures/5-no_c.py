#!/usr/bin/python3
def no_c(my_string):
    Thi_nstring = my_string.translate({ord(i): None for i in 'cC'})
    return Thi_nstring
