#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                division_result = 0
                try:
                    division_result = element_1 / element_2
                except ZeroDivisionError:
                    print("division by 0")
                except (TypeError, ValueError):
                    print("wrong type")
                finally:
                    result_list.append(division_result)
            except IndexError:
                print("out of range")
                result_list.append(0)
    except Exception as e:
        pass
    finally:
        return result_list
