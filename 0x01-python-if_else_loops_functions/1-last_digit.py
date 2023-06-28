#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    dig = number * -1
    dig = dig % 10
    dig = dig * -1
else:
    dig = number % 10
print("Last digit of {}".format(number), end=' ')
if dig > 5:
    print("is {} and is greater than 5".format(dig))
elif dig == 0:
    print("is {} and is 0".format(dig))
elif dig < 6 and dig != 0:
    print("is {} and is less than 6 and not 0".format(dig))
