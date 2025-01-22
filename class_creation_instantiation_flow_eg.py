class MyMeta(type):
    def __new__(mcs, name, bases, dct):
        print("MyMeta.__new__ called")
        return super().__new__(mcs, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print("MyMeta.__init__ called")
        super().__init__(name, bases, dct)

class MyClass(metaclass=MyMeta):
    def __new__(cls, *args, **kwargs):
        print("MyClass.__new__ called")
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("MyClass.__init__ called")

# Instantiate the class
obj = MyClass()
