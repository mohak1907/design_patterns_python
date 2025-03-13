"""
Chain of Responsibility Pattern:

It is a behavioral design pattern that allows a request to be passed along a chain of handlers. Each handler
decides whether to process the request or pass it to the next handler in the chain.
This pattern helps decouple senders and receivers and allows multiple objects to handle a request without the
sender needing to know which handler will process it.

Key Components:
    1. Handler (Abstract Class)
        Defines the method to process the request.
        Stores a reference to the next handler in the chain.
    2. Concrete Handlers
        Implements the handler interface.
        Decides whether to process the request or pass it forward.
    3. Client (Requester)
        Creates the chain and sends the request.

Use Cases:
    ✅ Logging Systems (e.g., log to file, console, database based on severity).
    ✅ Middleware Processing (e.g., authentication, authorization, request validation).
    ✅ Customer Support Systems (e.g., handling complaints at different levels).
    ✅ Workflow Approval Systems (e.g., manager → director → CEO).

Advantages:
    ✅ Decouples Senders and Receivers: The sender doesn’t need to know which handler will process the request.
    ✅ Flexible and Scalable: Handlers can be added, removed, or modified without affecting other handlers.
    ✅ Improves Maintainability: Clear responsibility distribution.

Disadvantages:
    ❌ Request Might Go Unhandled: If no handler processes the request, it may get lost.
    ❌ Can Be Hard to Debug: Long chains make it harder to trace request flow.

An example where different authorization levels handle a request:
Explanation:
    1. Handler (Handler Abstract Class)
        Defines handle(request) and allows setting the next handler.
    2. Concrete Handlers (EmployeeHandler, ManagerHandler, DirectorHandler, CEOHandler)
        Each handler processes the request if it falls within its range.
        Otherwise, it forwards the request to the next handler.
    3. Client Code
        Sets up the chain dynamically.
        Sends different monetary requests, which get processed at the correct level.
"""
from abc import ABC, abstractmethod

# Handler Abstract Class
class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  # Allows method chaining

    @abstractmethod
    def handle(self, request):
        pass

# Concrete Handler 1: Employee Level
class EmployeeHandler(Handler):
    def handle(self, request):
        if request <= 1000:
            print(f"Employee approved the request of ${request}.")
        elif self.next_handler:
            self.next_handler.handle(request)

# Concrete Handler 2: Manager Level
class ManagerHandler(Handler):
    def handle(self, request):
        if request <= 5000:
            print(f"Manager approved the request of ${request}.")
        elif self.next_handler:
            self.next_handler.handle(request)

# Concrete Handler 3: Director Level
class DirectorHandler(Handler):
    def handle(self, request):
        if request <= 20000:
            print(f"Director approved the request of ${request}.")
        elif self.next_handler:
            self.next_handler.handle(request)

# Concrete Handler 4: CEO Level (Final Handler)
class CEOHandler(Handler):
    def handle(self, request):
        if request > 20000:
            print(f"CEO approved the request of ${request}.")
        else:
            print(f"Request of ${request} could not be processed.")

# Client Code
if __name__ == "__main__":
    # Creating the chain: Employee -> Manager -> Director -> CEO
    employee = EmployeeHandler()
    manager = ManagerHandler()
    director = DirectorHandler()
    ceo = CEOHandler()

    employee.set_next(manager).set_next(director).set_next(ceo)

    # Request scenarios
    requests = [500, 3000, 10000, 50000]
    for req in requests:
        print(f"\nProcessing request of ${req}:")
        employee.handle(req)  # Start from the first handler in the chain
