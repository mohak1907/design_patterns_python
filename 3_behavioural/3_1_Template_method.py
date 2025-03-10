'''
Template method Pattern:
This is a behavioral design pattern that defines the skeleton of an algorithm in a base class, but lets
subclasses provide the specific implementation for certain steps. This promotes code reuse while allowing
flexibility in the individual steps of the process.

Key Components:
    1. Abstract Class (Template Class)
        Defines the structure of the algorithm (the template method).
        Implements common logic.
        Leaves abstract methods for subclasses to implement.
    2. Concrete Subclasses
        Implement the abstract methods defined in the template.
        Customize specific steps of the algorithm.

Use Cases:
    ✅ Workflow automation (e.g., processing orders, data parsing).
    ✅ Game development (e.g., AI behavior patterns).
    ✅ Report generation with different formats.
    ✅ File processing pipelines.

Disadvantages:
    ❌ Rigid Structure: The overall flow cannot be changed without modifying the base class.
    ❌ Inheritance Dependency: Tightly couples subclasses to the base class.    
'''
import abc


class ThreeDaysTrip(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def transport(self):
        pass

    @abc.abstractmethod
    def day1(self):
        pass

    @abc.abstractmethod
    def day2(self):
        pass

    @abc.abstractmethod
    def day3(self):
        pass

    @abc.abstractmethod
    def back_to_home(self):
        pass

    def iternary(self):
        print("Trip is started")
        self.transport()
        self.day1()
        self.day2()
        self.day3()
        self.back_to_home()
        print("Trip is over")


class SouthTrip(ThreeDaysTrip):
    def transport(self):
        print("Go by train! check in to hotel")

    def day1(self):
        print("Day-1: Enjoy the hotel beach whole day")

    def day2(self):
        print("Day-2: Visit historical places and Enjoy cruise life at night")

    def day3(self):
        print("Day-3: Enjoy shopping day with family and go anywhere you wish")

    def back_to_home(self):
        print("Check out and go Home by air!")


class NorthTrip(ThreeDaysTrip):
    def transport(self):
        print("Go by air! check in to hotel")

    def day1(self):
        print("Day-1: Go to very highted place and enjoy snow activities")

    def day2(self):
        print("Day-2: Enjoy river rafting and lavish dinner at night")

    def day3(self):
        print("Day-3: Enjoy shopping day with family and go anywhere you wish")

    def back_to_home(self):
        print("Check out and go Home by air!")


if __name__ == "__main__":
    place = input("Where do you want to go (north/south) ?")
    if place == 'north':
        trip = NorthTrip()
        trip.iternary()
    elif place == 'south':
        trip = SouthTrip()
        trip.iternary()
    else:
        print(f"Sorry, We do not have any trip for {place}!")