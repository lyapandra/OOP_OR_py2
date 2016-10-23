class MyClass(object):
    '''to e Class
    '''

    var = 10
    def print_me(self):
        print __name__

this_obj_01 = MyClass()
print this_obj_01.var

this_obj_02 = MyClass()
print this_obj_02.var
this_obj_01.print_me()
for nm in range(len(dir(this_obj_01))):
    print nm, dir(this_obj_01)[nm], dir(this_obj_01)[nm], dir(dir(this_obj_01)[nm])
print 'v0', str.__doc__
print 'v1', this_obj_01.__doc__
#print 'v2', this_obj_01.dir(this_obj_01)[3]