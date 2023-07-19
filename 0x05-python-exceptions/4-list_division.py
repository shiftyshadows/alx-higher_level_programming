#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError("out of range")
                numerator = my_list_1[i]
                denominator = my_list_2[i]
                if not isinstance(numerator, (int, float))
                or not isinstance(denominator, (int, float)):
                    raise TypeError("wrong type")
                if denominator == 0:
                    raise ZeroDivisionError("division by 0")
                result_list.append(numerator / denominator)
            except IndexError:
                print("out of range")
                result_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except TypeError:
                print("wrong type")
                result_list.append(0)
    except Exception as e:
        pass
    finally:
        return result_list
