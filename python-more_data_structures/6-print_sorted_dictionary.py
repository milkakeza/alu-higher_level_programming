#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    kiz = list(a_dictionary.keys())
    kiz.sort()
    for key in kiz:
        print("{}: {}".format(key, a_dictionary[key]))
