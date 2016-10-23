class A(object):
    def dothis(self):
        print 'doing this in A'
class B(A):
    pass
class C(A):
    def dothis(self):
        print 'doing this in C'
class D(C):
    '''doca'''
    a = 10
    def __init__(self):
        self.a = 5
    def get_attr(self):
        print D.a, self.a
    print '=', a#, self.a

d = D()
d.dothis()
print D.mro()
'''
print D.__doc__
print D.__dict__
print dir(D)'''
print D.a
print d.a
d.get_attr()
#print a