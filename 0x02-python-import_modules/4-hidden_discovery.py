#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    file = dir(hidden_4)
    fil_no = len(file)
    for i in range(fil_no):
        if not file[i].startswith("__"):
            print(file[i])
