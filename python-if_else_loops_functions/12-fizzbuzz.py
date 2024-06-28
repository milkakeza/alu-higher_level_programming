#!/usr/bin/python3


def fizzbuzz():
    # This is gonna print nbrs from 1 to 100 but when a number is a multiple of 3, it prints fizz; when a nbr is a multiple of 5, it prints buzz; finally when it is a multiple of both, it prints fizzbuzz
    for nbr in range(1, 101):
        if nbr % 3 == 0 and nbr % 5 == 0:
            print("FizzBuzz ", end="")
        elif nbr % 3 == 0:
            print("Fizz ", end="")
        elif nbr % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(nbr), end="")
