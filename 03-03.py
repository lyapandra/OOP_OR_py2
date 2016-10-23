import random
class girl(object):
    def when_you_do_this(self):
        self.random = random.randint(1,50)
        print 'Maybe in', self.random, 'days'
    def callme(self):
        print 'I\'m here'
    greeting = 'hello, father'

Ira = girl()
#print Ira.greeting
#Ira.callme()
Ira.when_you_do_this()
