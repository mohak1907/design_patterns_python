"""
Pattern Type - Creational
Patern Name -  Singleton
Description - whenever we need a single instance of a class whenever we instantiate an object.
__new__ method is used to create the instance of the class, and is called before the object instance is
created. 
1_3_singleton.py style is prefered
"""


class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
o1 = SingleTon()
print("Object - 1 ==>", o1)
o1.data = 10

o2 = SingleTon()
print("Object - 2 ==>", o2)
print("Object - 2 data ==>", o2.data)
o2.data = 5

print("Object - 1 data ==>", o1.data)
