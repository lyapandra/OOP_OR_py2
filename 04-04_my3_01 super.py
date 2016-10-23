# Super is super (video) http://pythonz.net/videos/34/
''' '''
#from __future__ import print_function
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
#class OrderedCounter(OrderedDict, Counter):
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

oc = OrderedCounter('asdasdasdasd')
print oc
oc = Counter('asdasdasdasd')
print oc
oc = OrderedDict(oc)
print oc
help(OrderedCounter)
'''
print '='*80
help(Counter)
print '='*80
help(OrderedDict)
print '='*80'''