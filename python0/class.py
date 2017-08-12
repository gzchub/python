#!/usr/bin/python

class Person(object):
    age = 10
    name = "xiaoming"

    def color(self,c):
        print "xiaoming is %s"%c


boy = Person()

print boy.age

print boy.name

boy.color("black")
