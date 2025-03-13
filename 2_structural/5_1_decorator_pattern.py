"""
Decorator Design Pattern:
It is a structural design pattern that allows you to dynamically add behavior to objects without modifying
their structure. Instead of using subclassing, decorators use composition to wrap an object with additional
functionality.

Key Components:
    1. Component (Base Interface/Abstract Class)
        Defines the common interface for objects that can be decorated.
    2. Concrete Component
        The actual object that will be decorated.
    3. Decorator (Base Wrapper Class)
        Wraps the component and forwards requests.
    4. Concrete Decorators
        Extend functionality by wrapping the component dynamically.

Use Cases:
    ✅ Adding functionality dynamically (e.g., logging, authentication).
    ✅ UI elements (e.g., adding scrollbars, borders, themes).
    ✅ File I/O (e.g., compression, encryption, buffering).
    ✅ Game development (e.g., power-ups affecting characters).

Advantages:
    ✅ Dynamically add/remove behavior at runtime.
    ✅ Avoids subclass explosion (no need for multiple subclasses).
    ✅ Follows Open-Closed Principle (extend behavior without modifying existing code).

Disadvantages:
    ❌ Can become complex with multiple layers of decorators.
    ❌ Harder to debug due to multiple wrapping levels.

An example where we decorate a simple coffee with additional ingredients.
Explanation:
    1. Component (Coffee)
        Defines the interface for all coffee types.
    2. Concrete Component (SimpleCoffee)
        Implements a basic coffee with a fixed cost.
    3. Decorator (CoffeeDecorator)
        Wraps a Coffee object and forwards method calls.
    4. Concrete Decorators (MilkDecorator, SugarDecorator, VanillaDecorator)
        Extend the functionality by modifying cost() and description().
    5. Client Code
        Starts with a SimpleCoffee and dynamically adds Milk, Sugar, and Vanilla decorators.
"""
from abc import ABC, abstractmethod

# Component Interface (Base Class)
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete Component (Simple Coffee)
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base cost

    def description(self):
        return "Simple Coffee"

# Decorator (Base Wrapper)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Adds cost for milk

    def description(self):
        return self._coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Adds cost for sugar

    def description(self):
        return self._coffee.description() + ", Sugar"

class VanillaDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3  # Adds cost for vanilla

    def description(self):
        return self._coffee.description() + ", Vanilla"

# Usage Example
if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"{coffee.description()} - ${coffee.cost()}")

    coffee = MilkDecorator(coffee)
    print(f"{coffee.description()} - ${coffee.cost()}")

    coffee = SugarDecorator(coffee)
    print(f"{coffee.description()} - ${coffee.cost()}")

    coffee = VanillaDecorator(coffee)
    print(f"{coffee.description()} - ${coffee.cost()}")
