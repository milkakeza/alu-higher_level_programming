#!/usr/bin/python3
for i in range(0, 100):
    number = i
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
