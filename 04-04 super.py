import random
class Animal(object):
    def __init__(self,name):
        self.name = name
        self.breed = random.choice(['Zver_01', 'Zver_02', 'Zver_03'])
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name) # the same as <===> Animal.__init__(self, name) OR #self.name = name
        #self.breed = random.choice(['Zver_01', 'Zver_02', 'Zver_03'])
    def fetch(self, thing):
        print '{0} goes after {1}'.format(self.name, thing)
class Cat(Animal):
    pass
d = Dog('dogname')
c = Cat('kiza')
print d.name
print d.breed