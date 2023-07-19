#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if count >= x:
                break
            try:
                print("{:d}".format(element), end='')
                count += 1
            except (TypeError, ValueError):
                pass
    except Exception as e:
        return 0
    finally:
        print()
        return count
