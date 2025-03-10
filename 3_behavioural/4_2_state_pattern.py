"""
Example to implement a Media Player that can transition between different states (Playing, Paused, and Stopped)
using the State Design Pattern.

Scenario:
A media player has the following states:

    1. Playing State
        Can pause (transitions to Paused state).
        Can stop (transitions to Stopped state).
    2. Paused State
        Can resume (transitions back to Playing state).
        Can stop (transitions to Stopped state).
    3. Stopped State
        Can start playing (transitions to Playing state).

Each state is encapsulated in a separate class, making it easy to extend and modify.

"""

from abc import ABC, abstractmethod

# State Interface
class MediaPlayerState(ABC):
    @abstractmethod
    def play(self, context):
        pass

    @abstractmethod
    def pause(self, context):
        pass

    @abstractmethod
    def stop(self, context):
        pass

# Concrete State: Playing
class PlayingState(MediaPlayerState):
    def play(self, context):
        print("Already Playing!")

    def pause(self, context):
        print("Pausing Media...")
        context.state = PausedState()

    def stop(self, context):
        print("Stopping Media...")
        context.state = StoppedState()

# Concrete State: Paused
class PausedState(MediaPlayerState):
    def play(self, context):
        print("Resuming Media...")
        context.state = PlayingState()

    def pause(self, context):
        print("Already Paused!")

    def stop(self, context):
        print("Stopping Media from Paused State...")
        context.state = StoppedState()

# Concrete State: Stopped
class StoppedState(MediaPlayerState):
    def play(self, context):
        print("Starting Media...")
        context.state = PlayingState()

    def pause(self, context):
        print("Cannot Pause! Media is already stopped.")

    def stop(self, context):
        print("Media is already stopped!")

# Context: Media Player
class MediaPlayer:
    def __init__(self):
        self.state = StoppedState()  # Default state

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)

# Usage Example
if __name__ == "__main__":
    player = MediaPlayer()

    player.play()   # Starting Media...
    player.pause()  # Pausing Media...
    player.play()   # Resuming Media...
    player.stop()   # Stopping Media...
    player.pause()  # Cannot Pause! Media is already stopped.
