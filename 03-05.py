#incapsilation
class MyClass():
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        print self.val

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)
a.set_val('hi')
a.get_val()
#b.get_val()