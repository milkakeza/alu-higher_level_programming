#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    nume = 0
    deno = 0

    for tpl in my_list:
        nume += tpl[0] * tpl[1]
        deno += tpl[1]

    return (nume / deno)
