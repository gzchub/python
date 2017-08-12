#!/usr/bin/python

import module1 as m
from module2 import D
#reload(module1)

print m.a

obj = m.A()

obj.a()

m.b()

a = 10

print m.__doc__

print "====================================================>>>"

obj_d = D()
obj_d.d()
