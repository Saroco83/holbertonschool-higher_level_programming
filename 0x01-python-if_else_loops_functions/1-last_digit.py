#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number <= 0:
    positiveNum = number * (-1)
    LastNum = positiveNum % 10
    LastNum = LastNum * (-1)
    if LastNum < 6 and LastNum != 0:
        print("Last digit of {} is {} and is\
 less than 6 and not 0".format(number, LastNum))
    else:
        print("Last digit of {} is {} and is 0".format(number, LastNum))
else:
    LastNum = number % 10
    if LastNum > 5:
        print("Last digit of {} is {} and is\
 greater than 5".format(number, LastNum))
    elif LastNum == 0:
        print("Last digit of {} is {} and is 0".format(number, LastNum))
    else:
        print("Last digit of {} is {} and is\
 less than 6 and not 0".format(number, LastNum))
