class Base:
    def save(self):
        print "saving base"


class A:
    something = "hi"

    def __init__(self):
        print 'A'

    def save(self):
        print "saving A"


class B:
    def __init__(self):
        print 'B'


class C(A, Base): pass


class D(Base, B, A): pass


c = C() # prints 'A'
d = D() # prints 'B'

c.save()
d.save()
