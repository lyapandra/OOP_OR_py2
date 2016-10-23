# Super is super (video) http://pythonz.net/videos/34/
'''add OrganicDoughFactory'''
from pizza import Pizza, DoughFactory

class OrganicDoughFactory(object):
    def get_dough(self):
        return 'pure intreated wheat dough'
class DoughFactory(object):
    '''add SUPER'''
    def get_dough(self):
        return 'insecticide treated wheat dough'
class Pizza(DoughFactory):
    def order_pizza(self, *toppings):
        print 'Getting dough'
        dough = super(Pizza, self).get_dough() #was "dough = DoughFactory.get_dough(self)"
        print 'making pie with %s' % dough
        for topping in toppings:
            print  'Adding: %s' % topping
class OrganicPizza(Pizza, OrganicDoughFactory): pass
'''
if __name__ == '__main__':
    Pizza().order_pizza('Papperoni', 'Ternopil Pizza')
    help(Pizza)'''
if __name__ == '__main__':
    OrganicPizza().order_pizza('Papperoni', 'Ternopil Pizza')
    help(OrganicPizza)

#help(Pizza)
#help(Rachel)