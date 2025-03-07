"""
Handling Multiple Commands in a Queue
In this advanced example, we will extend the Command pattern to handle multiple commands in a queue,
allowing batch execution and undo functionality.

Scenario:
    We have a Smart Home System that can turn on/off lights and music, and we want to:
        1. Queue multiple commands before executing them.
        2. Execute all commands at once (like a macro function).
        3. Support undoing the last batch of commands.
"""

from abc import ABC, abstractmethod
from collections import deque


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver 1: Light
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Receiver 2: Music System
class MusicSystem:
    def play_music(self):
        print("Music is PLAYING")

    def stop_music(self):
        print("Music is STOPPED")

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

class MusicPlayCommand(Command):
    def __init__(self, music_system: MusicSystem):
        self.music_system = music_system

    def execute(self):
        self.music_system.play_music()

    def undo(self):
        self.music_system.stop_music()

class MusicStopCommand(Command):
    def __init__(self, music_system: MusicSystem):
        self.music_system = music_system

    def execute(self):
        self.music_system.stop_music()

    def undo(self):
        self.music_system.play_music()

# Invoker: Smart Home Remote with a Command Queue
class SmartHomeRemote:
    def __init__(self):
        self.command_queue = deque()
        self.executed_commands = deque()

    def add_command(self, command: Command):
        self.command_queue.append(command)

    def execute_all(self):
        print("\nExecuting Commands:")
        while self.command_queue:
            command = self.command_queue.popleft()
            command.execute()
            self.executed_commands.append(command)

    def undo_last_batch(self):
        print("\nUndoing Last Batch:")
        while self.executed_commands:
            command = self.executed_commands.popleft()
            command.undo()

# Usage Example
if __name__ == "__main__":
    light = Light()
    music = MusicSystem()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    music_play = MusicPlayCommand(music)
    music_stop = MusicStopCommand(music)

    remote = SmartHomeRemote()

    # Add commands to the queue
    remote.add_command(light_on)
    remote.add_command(music_play)

    # Execute all commands
    remote.execute_all()

    # Undo last batch
    remote.undo_last_batch()

    # Add more commands
    remote.add_command(light_off)
    remote.add_command(music_stop)

    # Execute the new commands
    remote.execute_all()

    # Undo last batch again
    remote.undo_last_batch()
