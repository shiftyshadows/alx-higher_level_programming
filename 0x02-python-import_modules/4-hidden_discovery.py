#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    file = dir(hidden_4)
    fil_no = len(file)
    for i in range(0, fil_no):
        if file[i][0:2] != "__":
            print(file[i])
