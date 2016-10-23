class Car(object):
    def __init__(self, owner, door):
        self.owner = owner
        self.door = 'closed'
    speed = 0
    def get_door_state(self):
        print self.owner, 'door is', self.door,
    '''
    def gas(self):
        self.speed += 10
    def beee(self):
        print 'be'
    '''
class Hundai(Car):
    def door_key_r(self):
        self.door = 'opened'
        self.get_door_state()
    def door_key_l(self):
        self.door = 'closed'
        self.get_door_state()
class VAZ(Car):
    def door_key_r(self):
        self.door = 'closed'
        self.get_door_state()
    def door_key_l(self):
        self.door = 'opened'
        self.get_door_state()

father_car = VAZ('father','closed')
#father_car.owner = 'father'
mother_car = Hundai('mather','closed')
#mother_car.owner = 'mather'

print 'door m',mother_car.door
mother_car.door_key_r()

print '\ndoor f', father_car.door
father_car.door_key_l()
print '\ndoor m',mother_car.door
print '\ndoor f', father_car.door
'''
print father_car.speed
#father_car.speed = 10
father_car.gas()
father_car.gas()
print father_car.speed

print mother_car.speed
#mother_car.speed = 10
#mother_car.gas()
mother_car.gas()
print mother_car.speed
'''