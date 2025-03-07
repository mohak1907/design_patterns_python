"""
Learn how to create simple factory which helps to hide
logic of creating objects.
"""

from abc import ABCMeta, abstractmethod

class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass


class BE(AbstractDegree):
    def info(self):
        print("Bachelor of engineering")

    def __str__(self):
        return "Bachelor of engineering"

class ME(AbstractDegree):
    def info(self):
        print("Master of engineering")

    def __str__(self):
        return "Master of engineering"


class MBA(AbstractDegree):
    def info(self):
        print("Master of business administration")

    def __str__(self):
        return "Master of business administration"



class ProfileAbstractFactory(object):
    def __init__(self):
        self._degrees = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def addDegree(self, degree):
        self._degrees.append(degree)

    def getDegrees(self):
        return self._degrees


class ManagerFactory(ProfileAbstractFactory):
    def createProfile(self):
        """ This method will be called whenever object of this class is created,
        as in Parent class constructor this method is called"""
        self.addDegree(BE())
        self.addDegree(MBA())

class EngineerFactory(ProfileAbstractFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(ME())

class ProfileCreatorFactory(object):
    class_list = {'ManagerFactory': globals().get('ManagerFactory'),
                  'EngineerFactory': globals().get('EngineerFactory')}

    @classmethod
    def create_profile(cls, name):
        return eval(profile_type + 'Factory', {}, cls.class_list)()
        


if __name__ == '__main__':
    profile_type = input("Which Profile would you like to create? Manager/Engineer - ")
    try:
        profile = ProfileCreatorFactory.create_profile(profile_type)
        print("Creating Profile of ", profile_type)
        print("Profile has following degrees -")
        for deg in profile.getDegrees():
            # print(type(deg))
            print('- ', deg)
    except NameError as e:
            print(e)