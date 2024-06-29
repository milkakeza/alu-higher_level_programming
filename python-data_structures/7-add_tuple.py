#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newtuple = ()
    fst_tuple = tuple_a + (0, 0)
    scndtuple = tuple_b + (0, 0)
    newtuple = fst_tuple[0] + scndtuple[0], fst_tuple[1] + scndtuple[1]
    return newtuple
