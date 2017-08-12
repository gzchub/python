a = 1

def out():
    b = 2
    def inner():
        nonlocal b
        b += 10
        print (b)
    inner()
out()
