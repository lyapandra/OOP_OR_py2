# Super is super (video) http://pythonz.net/videos/34/
''' '''
class Robot(object):
    def fetch(selfself, tool): print ('fetch')
    def move_forward(selfself, tool): print ('move_forward')
    def move_backward(selfself, tool): print ('move_backward')
    def replace(selfself, tool): print ('replace')

class CleaningRobot(Robot):
    def clean(self, tool, times = 3):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)

class MockRobot(Robot):
    def fetch(selfself, tool): print ('fetch_2')
    def move_forward(selfself, tool): print ('move_forward')
    def move_backward(selfself, tool): print ('move_backward')
    def replace(selfself, tool): print ('replace')
class MockCleaningRobot(CleaningRobot, MockRobot): pass

if __name__ == '__main__':
    #t = CleaningRobot()
    #t.clean('brooms')
    r = MockCleaningRobot()
    r.fetch('brooms')
    #r.clean('brooms')
    help(MockCleaningRobot)
