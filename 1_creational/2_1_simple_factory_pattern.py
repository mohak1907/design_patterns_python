"""
Factory pattern is creational design pattern which help hiding object creation process.
Benefits:-
Object creating can be independant from that of class implementation. 
"""

"""
Learn how to create simple factory which helps to hide logic of creating objects.
Using Abstract Class here.
Objects of HR & Engineer are created here by user without explicitly creating the objects

eval() method is used to convert string expression to the executable expression
eg:
y = "x>5"
x = 6
print(eval(x)) -> True

inbuilts methods:-
locals()-> returns local scope variables/methods including dunder ones
globals() -> returns global scope variable/methods including dunder  ones
"""

from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class HR(Person):
    def create(self, name):
        print(f"HR {name} is created")

class Engineer(Person):
    def create(self, name):
        print(f"Engineer {name} is created")

class PersonFactory(object):
    class_list = {'HR': globals().get('HR'), 'Employee': globals().get('Employee')}

    @classmethod
    def createPerson(cls, designation, name):
        try:
            obj = eval(designation, {}, cls.class_list)()
            # cls.list as locals give the validation that only string specified in this dictionary is allowed
            # otherwise NameError Exception will be raised
            obj.create(name)
        except NameError as e:
            print(e)


if __name__ == "__main__":
    designation = input("Please enter the designation - ")
    name = input("Please enter the person's name - ")
    PersonFactory.createPerson(designation, name)