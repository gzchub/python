#!/usr/bin/python


class ParentClass(object):
    name = "老张"

    def func(self):
        print "老子有钱"

class ChildClass(ParentCalss):
    name = "小张"

    def fun(self):
        print "哥也有钱"

class GrentChildClass(ChildClass):
    pass


child = ChildClass()

print child.name

child.func()

grent_child = GrentChildClass()

print grent_child.name
