"""
Memento Design Pattern

It is a behavioral design pattern that allows an object to save and restore its state without exposing its
internal details. This pattern is commonly used for undo/redo functionality in applications.

Key Components:
    1. Originator (The Object with State)
        Creates and restores snapshots (mementos) of its state.
    2. Memento (Snapshot)
        Stores the state of the originator.
        Is immutable (should not be modified once created).
    3. Caretaker (Manages Mementos)
        Stores mementos and restores them when needed.
        Maintains a history of saved states.

Use Cases:
    ✅ Undo/Redo functionality (text editors, games, design tools).
    ✅ State recovery (saving game progress, restoring previous configurations).
    ✅ Checkpointing (bank transactions, workflow management).

Advantages:
    ✅ Encapsulates State: Originator’s state is saved/restored without exposing internal details.
    ✅ Supports Undo/Redo: Provides checkpointing for restoring previous states.
    ✅ Encourages History Tracking: Maintains a list of past states for rollback.

Disadvantages:
    ❌ Can Consume Memory: Storing multiple snapshots may require large storage.
    ❌ May Require Deep Copying: Large objects may require deep copying for accurate state restoration.

An example where a Text Editor supports undo functionality using the Memento Pattern.
Explanation:
    1. Memento (Memento)
        Stores a snapshot of the editor's text.
    2. Originator (TextEditor)
        Writes text.
        Creates mementos to save its state.
        Restores previous states from mementos.
    3. Caretaker (History)
        Maintains a stack of mementos for undo functionality.
        Saves mementos and pops them when undoing.
    4. Client Code
        Writes text, saves states, and performs undo operations.
"""
# Memento: Stores the state
class Memento:
    def __init__(self, text):
        self._text = text

    def get_saved_text(self):
        return self._text

# Originator: The object that holds the state
class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, new_text):
        self._text = new_text

    def save(self):
        return Memento(self._text)  # Create a snapshot

    def restore(self, memento):
        self._text = memento.get_saved_text()

    def __str__(self):
        return f"Editor Content: {self._text}"

# Caretaker: Manages undo history
class CareTaker:
    def __init__(self):
        self._mementos = []

    def save_state(self, memento):
        self._mementos.append(memento)

    def undo(self):
        if self._mementos:
            return self._mementos.pop()
        return None  # No state to restore

# Usage Example
if __name__ == "__main__":
    editor = TextEditor()
    history = CareTaker()

    # Writing text
    editor.write("Hello, World!")
    print("save memento - Hello, World!")
    history.save_state(editor.save())  # Save state

    editor.write("Hello, Python!")
    print("save memento - Hello, Python!")
    history.save_state(editor.save())  # Save state

    editor.write("Hello, AI!")  # No save

    print(editor)  # Current state

    print("restore last memento")

    # Undo last change
    editor.restore(history.undo())
    print(editor)  # After first undo

    # Undo again
    print("restore last memento")
    editor.restore(history.undo())
    print(editor)  # After second undo
