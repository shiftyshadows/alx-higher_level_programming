#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if count < x:
                print(element, end='')
                count += 1
    except Exception as e:
        pass
    finally:
        print()
        return count
