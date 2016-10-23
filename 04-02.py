class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print '%s is eating %s' % (self.name, food)
class Dog(Animal):
    def fetch(self, thing):
        print '%s goes after %s' % (self.name, thing)
class Cat(Animal):
    def shred(self):
        print '%s shreds something' % (self.name)
d = Dog('4arlik')
c = Cat('Kitza')
d.fetch('paper')
d.eat('bones')
c.eat('liver')
c.shred()
#d.shred()
