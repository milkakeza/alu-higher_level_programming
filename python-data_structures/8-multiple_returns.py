#!/usr/bin/python3
def multiple_returns(sentence):
    Thi_tuple = ()
    if len(sentence) == 0:
        Thi_tuple = 0, "None"
    else:
        Thi_tuple = len(sentence), sentence[0]
    return Thi_tuple
