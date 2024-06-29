#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        MaList = list(a_dictionary.keys())
        best_score = 0
        key = ""
        for i in Malist:
            if a_dictionary[i] > best_score:
                best_score = a_dictionary[i]
                key = i
        return key
