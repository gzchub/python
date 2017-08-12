#coding=utf-8
import datetime

def begin(func):
    def wrapper():
        print "现在时间:"
        func()
    return wrapper

@begin
def getTime():
    print datetime.datetime.now()


# begin (getTime)()
getTime()
