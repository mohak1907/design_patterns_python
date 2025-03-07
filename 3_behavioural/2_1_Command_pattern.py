'''
Command Design Pattern:
This is a behavioral design pattern that turns a request into a standalone object, encapsulating all
information about the request. This allows requests to be parameterized, delayed, queued, logged, and even
undone or redone.

Key Components:
    1. Command (Interface/Abstract Class)
        Declares an execute() method that all concrete commands must implement.
    2. Concrete Command
        Implements the execute() method to perform a specific action.
        May also have an undo() method to reverse the action.
    3. Receiver
        The actual business logic or component that performs the request's action.
    4. Invoker
        Keeps track of commands and invokes their execute() method.
        Can optionally support undo() functionality.
    5. Client
        Creates and configures command objects.
        Passes command objects to the invoker.

Use Cases:
    ✅ GUI buttons and menus (Undo/Redo operations).
    ✅ Task scheduling (Queueing commands for later execution).
    ✅ Macro recording (Executing multiple commands in sequence).
    ✅ Remote control systems (TV remote, smart home devices).

Disadvantages
    ❌ Can increase the number of classes (one for each command).
    ❌ May introduce unnecessary complexity for simple tasks.
'''

from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver (The actual logic)
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker (Stores and executes commands)
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()

# Usage Example
if __name__ == "__main__":
    light = Light()
    
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    
    remote = RemoteControl()
    
    remote.set_command(light_on)
    remote.press_button()  # Light is ON
    remote.press_undo()    # Light is OFF
    
    remote.set_command(light_off)
    remote.press_button()  # Light is OFF
    remote.press_undo()    # Light is ON
