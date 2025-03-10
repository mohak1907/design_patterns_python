"""
State Design Patttern:

Main Class:
    Will initialize the state object
    self will be attached to that state
State Interface Class:
    will provide few abstract methods for actions
Concrete State Class:
    will implement real logic for a particular state inheriting from the interface class
"""

from abc import ABC, abstractmethod

# State Interface
class State(ABC):

    @abstractmethod
    def push_down_btn(self) -> None:
        pass

    @abstractmethod
    def push_up_btn(self) -> None:
        pass
    
# Context: Main class
class Elevator:

    _state = None

    def __init__(self, state: State) -> None:
        self.set_elevator(state)

    def set_elevator(self, state: State):
        self._state = state
        self._state.elevator = self

    def present_state(self):
        print(f"Elevator is on {type(self._state).__name__}")

    def push_down_btn(self):
        self._state.push_down_btn()

    def push_up_btn(self):
        self._state.push_up_btn()
        
# Concrete State:        
class GroundFloor(State):

    def push_down_btn(self) -> None:
        print("Already on the Ground floor")

    def push_up_btn(self) -> None:
        print("Elevator moving upward one floor.")
        self.elevator.set_elevator(FirstFloor())

# Concrete State:
class FirstFloor(State):

    def push_down_btn(self) -> None:
        print("Elevator moving down one floor.")
        self.elevator.set_elevator(GroundFloor())

    def push_up_btn(self) -> None:
        print("Elevator moving upward one floor.")
        self.elevator.set_elevator(SecondFloor())

# Concrete State:
class SecondFloor(State):

    def push_down_btn(self) -> None:
        print("Elevator moving down a floor...")
        self.elevator.set_elevator(FirstFloor())

    def push_up_btn(self) -> None:
        print("Already on the top floor")


if __name__ == "__main__":

    myElevator = Elevator(GroundFloor())
    myElevator.present_state()
    myElevator.push_up_btn()
    myElevator.push_up_btn()
    myElevator.present_state()
    myElevator.push_down_btn()
    myElevator.present_state()