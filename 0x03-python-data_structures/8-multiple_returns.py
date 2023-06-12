#!/usr/in/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        result = len(sentence), None
        return result
    else:
        result = len(sentence), sentence[0]
        return result
