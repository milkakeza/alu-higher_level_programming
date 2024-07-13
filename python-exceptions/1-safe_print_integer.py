#!/usr/bin/python3


def safe_print_integer(value):
    """ value variable will be of integer data type """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
