class A(object):
    def __getattr__(self,name):
        print "You use getattr"
        return "NO"

    def __setattr__(self,name,value):
        print "You use setattr"
        self.__dict__[name] = value

a = A()

print a.k
a.x = "set x"

del a.k
