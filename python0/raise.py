#!/usr/bin/python

class MyError(Exception):
    pass

s = raw_input()

try:
    if s == "error":
        print "This is my error"
        raise MyError("no error mesage")
    else:
        print s
except MyError as e:
    print "Error message:"
    print e 
