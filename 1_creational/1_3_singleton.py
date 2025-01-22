"""
Pattern name - SingleTon
Pattern type - Creational Design Pattern
Description - Using decorator class with a __call__method to overwrite the object instance.
__call__ method is used to handle the call() operation on an object.
eg. class A:
      pass
    a = A()
    a() -> here __call__ method will be called.
"""


# Solution - 3
class SingletonDecorator(object):
    def __init__(self, klass):
        print("__init__ is called")
        self.klass = klass
        self.instance = None
        
    def __call__(self, *args, **kwargs):
        print("__call__ is called")
        if self.instance == None:
            self.instance = self.klass(*args,**kwargs)
        return self.instance


@SingletonDecorator
class Logger(object):
    def __init__(self):
        print("__init__ of Logger is called")
        self.start = None

    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)

logger1 = Logger()
logger1.start = "# >"
print("Logger 1", logger1)
logger1.write("Logger1 object is created.")

logger2 = Logger()
logger2.start = "$ >"
print("Logger 2", logger2)
logger1.write("Logger2 object is created.")