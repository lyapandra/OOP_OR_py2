#incapsilation
class MyClass():
    classy = 10
    def set_insty(self):
        self.insty = 100

a = MyClass()

a.set_insty()
a.classy = 0
a.insty = 0
del a.classy
#del a.insty
print a.classy
print a.insty
