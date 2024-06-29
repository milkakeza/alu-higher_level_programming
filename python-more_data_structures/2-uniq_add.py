#!/usr/bin/python3


def uniq_add(my_list=[]):

    List = []
    sum = 0
    for nbr in my_list:
        if nbr not in List:
            sum += nbr
            List.append(nbr)
    return sum
