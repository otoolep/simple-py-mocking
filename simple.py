#!/usr/bin/env python

import mock

class MyClass(object):
    def one(self):
        return 1

    def two(self):
        return 2

    def three(self):
        return 3

def no_mocking():
    c = MyClass()
    print c.one()
    print c.two()

@mock.patch('__main__.MyClass.one', return_value=666)
def mocking_one(one):
    print one()

@mock.patch('__main__.MyClass')
def mocking_myclass(MockMyClass):
    m = MockMyClass()
    m.one.return_value = 777
    print m.one()
    print m.two()

@mock.patch.object(MyClass, 'one')
def mocking_myclass_object(one):
    c = MyClass()
    one.return_value = 888
    print c.one()
    print c.two()

@mock.patch.object(MyClass, 'one')
@mock.patch.object(MyClass, 'two')
def mocking_myclass_object_both_methods(two, one):
    c = MyClass()
    one.return_value = 111
    two.return_value = 222
    print c.one()
    print c.two()
    print c.three()

if __name__ == '__main__':
    no_mocking()
    print
    mocking_one()
    print
    mocking_myclass()
    print
    mocking_myclass_object()
    print
    mocking_myclass_object_both_methods()
