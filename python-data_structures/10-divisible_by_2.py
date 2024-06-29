#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisibleby2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisibleby2.append(True)
        else:
            divisibleby2.append(False)
    return divisibleby2
