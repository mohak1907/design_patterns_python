"""
Pattern name - SingleTon (Mono state pattern)
Pattern type - Creational Design Pattern
Description - here two classes will be made, and Parent class will share the attributes by using the __dict__ method.
__dict__ store an object's (writable) attributes i.e. variable, methods, special/dunder methods' name and values.
"""

# Solution - 2
class Borg(object):
    _shared = {}

    def __init__(self):
        self.__dict__ = self._shared


class SingleTon(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    # def __str__(self):
    #     return "<{} - Object>".format(self.val)


o1 = SingleTon("Hardik")
print("Object - 1 ==>", o1)
print("Object - 1 val ==>", o1.val)
print(o1.__dict__)


o2 = SingleTon("Aarav")
print("Object - 2 ==>", o2)
print("Object - 2 val ==>", o2.val)
print("Object - 1 val ==>", o1.val)

print(o1.__dict__)
print(o2.__dict__)