"""
Flyweight Design Patern:

It is a structural design pattern that minimizes memory usage by sharing common data among multiple objects.
Instead of creating multiple copies of identical objects, it stores shared intrinsic data in a single place
and allows objects to reference it.

Key Components:
    1. Flyweight (Shared Object)
        Stores intrinsic state (shared data that does not change).
        Provides methods to manipulate extrinsic state (unique data for each object).
    2. Concrete Flyweight
        Implements the flyweight interface and defines the shared data.
    3. Flyweight Factory
        Manages a pool of shared objects (caching & reusing them).
    4. Client
        Requests flyweight objects from the factory.
        Provides extrinsic data while reusing intrinsic data.

Use Cases:
    ✅ Text Processing (reusing character objects instead of creating new ones).
    ✅ Graphics Rendering (e.g., reusing sprites for trees in a game).
    ✅ Document Editors (e.g., storing formatting styles efficiently).
    ✅ Database Connection Pooling (reusing database connections).

Advantages:
    ✅ Memory Efficient: Reduces memory usage by sharing objects.
    ✅ Improves Performance: Avoids unnecessary object creation.
    ✅ Great for Large-Scale Objects: Ideal for game development, UI rendering, etc.

Disadvantages:
    ❌ Increased Complexity: Requires managing shared objects efficiently.
    ❌ Only Useful in Specific Cases: If objects have many unique attributes, the pattern may not be
    beneficial.

An example where we use the Flyweight Pattern to optimize memory usage for Tree objects in a forest.
Explanation:
    1. Flyweight (TreeType)
        Stores intrinsic data (tree name, color, texture).
        Multiple trees share the same TreeType object.
    2. Flyweight Factory (TreeFactory)
        Manages a pool of TreeType objects.
        Ensures duplicate trees reuse the same TreeType.
    3. Client (Tree)
        Stores extrinsic data (position: x, y).
        References a shared TreeType object instead of duplicating it.
    4. Usage (Forest)
        Creates trees efficiently, reusing shared tree types.
"""

class TreeType:
    """Flyweight class that stores shared (intrinsic) data."""
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def display(self, x, y):
        print(f"Tree '{self.name}' with color: {self.color}, texture: {self.texture} at ({x}, {y})")

# Flyweight Factory: Manages a pool of shared TreeType objects
class TreeFactory:
    _tree_types: dict[tuple, TreeType] = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = (name, color, texture)
        if key not in TreeFactory._tree_types:
            TreeFactory._tree_types[key] = TreeType(name, color, texture)
        return TreeFactory._tree_types[key]

# Client: Uses shared TreeType objects while keeping unique position data
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type  # Shared object

    def display(self):
        print(f"  ID of Tree Type: {id(self.tree_type)}")
        self.tree_type.display(self.x, self.y)

# Forest: Manages all tree objects
class Forest:
    def __init__(self):
        self.trees: list[Tree] = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def display(self):
        for tree in self.trees:
            tree.display()

# Usage Example
if __name__ == "__main__":
    forest = Forest()

    # Planting trees (some will share the same type)
    forest.plant_tree(1, 1, "Oak", "Green", "Rough")
    forest.plant_tree(2, 3, "Oak", "Green", "Rough")  # Reuses the same Oak type
    forest.plant_tree(5, 2, "Pine", "Dark Green", "Smooth")
    forest.plant_tree(3, 4, "Oak", "Green", "Rough")  # Reuses the same Oak type

    forest.display()
