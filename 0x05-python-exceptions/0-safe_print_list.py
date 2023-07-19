#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if count < x:
                print(element)
                count += 1
    except:
        pass
    finally:
        print()
        return count
