#!/usr/bin/python3
def print_last_digit(number):
    if number < 1:
        number *= (-1)
    m = number % 10
    print("{}".format(m), end="")
    return m
