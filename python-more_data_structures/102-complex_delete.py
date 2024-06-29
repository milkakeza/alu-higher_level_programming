#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    Lkeys = list(a_dictionary.keys())

    for K in Lkeys:
        if value == a_dictionary.get(K):
            del a_dictionary[K]

    return (a_dictionary)
