class Animal(object):
    def __init__(self,name):
        self.name = name
    years = 0
    def eat(self,food):
        print '{0} is eating {1}'.format(self.name, food)
class Dog(Animal):
    '''    def __init__(self, name, years):
        years = self.years
        self.name = name
    '''
    def fetch(self, thing):
        print '{0} goes after {1}'.format(self.name, thing)
    def show_affection(self):
        print '{0} wags tail'.format(self.name)
class Cat(Animal):
    def shred(self):
        print '%s shreds something'.format(self.name)
    def show_affection(self):
        print '{0} purrs MyaU-u0u'.format(self.name)

for a in (Dog('4arlik'), Cat('Kitza'), Cat('Mur4ik')):
    a.show_affection()
    a.eat('meat')
    print a.years