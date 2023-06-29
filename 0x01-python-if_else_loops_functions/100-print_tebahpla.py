#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    print("{}{}".format(chr(i), chr(i - 32)) if i % 2 == 1 else '', end='')
