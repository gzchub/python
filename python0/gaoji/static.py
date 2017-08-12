#coding=utf-8

class TestStaticMethod(object):
    @staticmethod
    def foo():
        print "calling static method foo()"

    #foo = staticmethod(foo)

class Child(TestStaticMethod):
    pass

static = TestStaticMethod()

static.foo()
TestStaticMethod.foo()


child = child()

child.foo()

print "============================================="
class TestStaticMethod(object):
    @classmethod
    def foo(cls):
        print "calling class method foo()"
        print cls.__name__

class Child1(TestStaticMethod):
    pass

cls = TestStaticMethod()

cls.foo()
