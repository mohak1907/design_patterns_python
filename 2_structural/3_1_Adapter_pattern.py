"""
Adapter Design Pattern:
This is a a structural design pattern that allows two incompatible interfaces to work together by providing
a bridge (adapter) between them. It acts as a wrapper around an existing class to make it compatible with a
different interface.

Key Components:
    1. Target (Client Interface)
        The interface expected by the client.
    2. Adaptee (Existing/Legacy Class)
        The existing component with an incompatible interface.
    3. Adapter (Wrapper Class)
        Converts the interface of the Adaptee into the Target interface.

Use Cases:
    ✅ Connecting new software with legacy systems.
    ✅ Integrating third-party APIs that do not match your existing system.
    ✅ Making classes with incompatible interfaces work together.
    ✅ Bridging differences between different data formats.
    ✅ Useful in real-world problems like database migrations or file format conversions.

Disadvantages:
    ❌ Extra Complexity: Introduces another layer of abstraction.
    ❌ May Impact Performance: If used excessively, wrapping calls adds overhead.
"""

# Adaptee (Existing Legacy Class)
class OldPrinter:
    def print_legacy(self, text):
        print(f"Old Printer Output: {text}")

# Target Interface (New System expects this)
class NewPrinter:
    def print_modern(self, text):
        pass  # Expected to be implemented

# Adapter (Adapts OldPrinter to NewPrinter)
class PrinterAdapter(NewPrinter):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print_modern(self, text):
        self.old_printer.print_legacy(text)  # Converts old method to new

# Client Code (Using Adapter)
if __name__ == "__main__":
    old_printer = OldPrinter()
    adapter = PrinterAdapter(old_printer)

    # Client expects a modern interface but gets an adapted old printer
    adapter.print_modern("Hello, World!")
