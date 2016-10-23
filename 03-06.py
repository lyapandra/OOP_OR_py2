class MyNum(object):
    def __init__(self, value):
        print 'calling __init__'
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value
    def __docs__(self):
        print 'docs'
    def increment(self):
        self.val += self.val

dd = MyNum('5')
dd.increment()
dd.increment()
print dd.val