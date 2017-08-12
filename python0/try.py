#!/usr/bin/python

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "zero can not be divsion"
result = div(3,0)
print result
