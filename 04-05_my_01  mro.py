class A(object): pass
class B(A): pass
class C(A): pass
class D(C): pass
class E(C): pass
class DD(D):
    def __init__(self):
        super(DD, self)
    def a():
        pass

#help(DD)
print DD.mro()