#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newtuple = ()
    1st_tuple = tuple_a + (0, 0)
    2ndtuple = tuple_b + (0, 0)
    newtuple = 1st_tuple[0] + 2ndtuple[0], 1st_tuple[1] + 2ndtuple[1]
    return newtuple
