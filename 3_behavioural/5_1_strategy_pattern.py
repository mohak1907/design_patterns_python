"""
Strategy Design Pattern:
It is a behavioral design pattern that allows a class to change its behavior at runtime by selecting from
multiple interchangeable algorithms (strategies). Instead of using if-else conditions to decide which
algorithm to use, the pattern encapsulates each algorithm in its own class and makes them interchangeable.

Key Components:
    1. Strategy Interface (Abstract Class)
        Defines a common interface for all algorithms(strategies).
    2. Concrete Strategies
        Implement different variations of the algorithm.
    3. Context (Main Class)
        Maintains a reference to the selected strategy.
        Can switch strategies dynamically at runtime.
        No need to change code of this for addition of any new Strategy

Use Cases:
    ✅ Payment processing (choosing between Credit Card, PayPal, or Bitcoin).
    ✅ Sorting algorithms (selecting Bubble Sort, Quick Sort, or Merge Sort).
    ✅ Discount strategies (applying percentage-based, fixed amount, or no discount).
    ✅ AI decision-making (e.g., different attack strategies in a game).

Disadvantages:
    ❌ User should know how each strategy are different to each other.
    ❌ More Classes: Each strategy requires a separate class.
    ❌ Overhead: Might introduce unnecessary complexity if only a few strategies exist.

Here is an example where we implement a payment system that supports different payment methods.

Explanation:
    1. Strategy Interface (PaymentStrategy)
        Defines a common pay() method for all payment strategies.
    2. Concrete Strategies (CreditCardPayment, PayPalPayment, BitcoinPayment)
        Implement different payment methods.
    3. Context (ShoppingCart)
        Stores a reference to a payment strategy.
        Calls the strategy’s pay() method when checkout() is invoked.
        Allows changing the strategy dynamically.
    4. Client (Main Program)
        Creates a ShoppingCart with a default payment method.
        Switches payment strategies dynamically.
"""

from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategy 1: Credit Card Payment
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

# Concrete Strategy 2: PayPal Payment
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")

# Concrete Strategy 3: Bitcoin Payment
class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Bitcoin.")

# Context: Shopping Cart
class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy  # Set default payment strategy

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy  # Change strategy dynamically

    def checkout(self, amount):
        self.strategy.pay(amount)  # Delegate payment processing

# Usage Example
if __name__ == "__main__":
    cart = ShoppingCart(CreditCardPayment())  # Default strategy

    cart.checkout(100)  # Paid $100 using Credit Card.

    cart.set_payment_strategy(PayPalPayment())  # Change strategy
    cart.checkout(200)  # Paid $200 using PayPal.

    cart.set_payment_strategy(BitcoinPayment())  # Change again
    cart.checkout(300)  # Paid $300 using Bitcoin.
