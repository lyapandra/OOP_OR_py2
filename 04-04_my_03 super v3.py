# Super is super (video) http://pythonz.net/videos/34/
class DoughFactory(object):
    def get_dough(self):
        return 'insecticide treated wheat dough'
class Pizza(DoughFactory):
    def order_pizza(self, *toppings):
        print ('Getting dough')
        dough = super().get_dough() #dough = DoughFactory.get_dough(self)
        #dough = self.get_dough()
        print ('making pie with %s' % dough)
        for topping in toppings:
            print  ('Adding: %s' % topping)

if __name__ == '__main__':
    Pizza().order_pizza('Papperoni', 'Ternopil Pizza')

#help(Pizza)
#help(Rachel)
