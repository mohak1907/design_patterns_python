"""
State Design Patttern:
is a behavioral design pattern that allows an object to change its behavior when its internal state
changes. Instead of using multiple conditional statements (e.g., if-else or switch), it encapsulates each
state as a separate class, promoting better maintainability and flexibility.

Key Components:
    1. Context (The Main Object)
        Maintains a reference to the current state object.
        Delegates state-specific behavior to the current state.
    2. State Interface (Abstract Class)
        Defines the common behavior for all states.
    3. Concrete States
        Implements behavior specific to each state.
        Can transition to other states.

Use Cases:
    ✅ Finite State Machines (FSM) (e.g., vending machines, traffic lights).
    ✅ UI Components (e.g., button states: enabled, disabled, hovered).
    ✅ Multiplayer Games (e.g., player states: idle, running, attacking).
    ✅ Document Workflow Systems (e.g., draft → review → published).

Disadvantages:
    ❌ Can Increase Class Count: Each state requires a new class.
    ❌ Overhead: Not ideal for simple state transitions.
"""

from abc import ABC, abstractmethod

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# Context: Traffic Light Controller
class TrafficLight:
    def __init__(self):
        self.state = RedLight()  # Initial state

    def change(self):
        self.state.handle(self)

# Concrete State: Red
class RedLight(TrafficLightState):
    def handle(self, context):
        print("Red Light: STOP!")
        context.state = GreenLight()  # Transition to Green

# Concrete State: Green
class GreenLight(TrafficLightState):
    def handle(self, context):
        print("Green Light: GO!")
        context.state = YellowLight()  # Transition to Yellow

# Concrete State: Yellow
class YellowLight(TrafficLightState):
    def handle(self, context):
        print("Yellow Light: SLOW DOWN!")
        context.state = RedLight()  # Transition to Red


# Usage Example
if __name__ == "__main__":
    traffic_light = TrafficLight()

    for _ in range(5):  # Simulate state changes
        traffic_light.change()
