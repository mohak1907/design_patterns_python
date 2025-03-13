"""
Builder Design Pattern:

It is a creational design pattern that separates the construction of a complex object from its representation.
It allows the step-by-step creation of an object while keeping the construction process flexible and reusable.

Key Components:
    1. Product (Complex Object)
        The object being built.
    2. Builder (Abstract Class or Interface)
        Defines the steps to construct the product.
    3. Concrete Builder
        Implements the builder interface and provides specific implementations.
    4. Director (Optional)
        Controls the construction process by invoking builder methods in a specific order.
    5. Client
        Uses the builder to construct complex objects.

Use Cases:
    ✅ Building complex objects step-by-step (e.g., reports, documents).
    ✅ Creating different representations of the same object (e.g., different car models).
    ✅ Configuring objects with multiple optional parameters (e.g., customizing UI components).
    ✅ Constructing hierarchical objects (e.g., XML, JSON structures).

Advantages:
    ✅ Simplifies Object Creation: Breaks down complex construction into manageable steps.
    ✅ Improves Code Readability: Uses method chaining for a fluent interface.
    ✅ Enforces Step-by-Step Construction: Ensures valid object construction.
    ✅ Supports Multiple Representations: Different builders for different configurations.

Disadvantages:
    ❌ More Code Overhead: Requires extra classes (Builder, Director).
    ❌ Overkill for Simple Objects: Not useful for objects with only a few attributes.

An example of using the Builder Pattern to construct a custom computer.
Explanation:
    1. Product (Computer)
        Represents the object being built.
    2. Builder Interface (ComputerBuilder)
        Defines the methods for constructing different parts of the computer.
    3. Concrete Builder (GamingComputerBuilder)
        Implements the builder interface.
        Uses method chaining (return self) to allow a fluent interface.
    4. Director (Director)
        Provides predefined configurations.
        Constructs an optimized gaming PC using the builder.
    5. Client Code
        Uses the builder directly or via the Director.

"""
# Product: Computer
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.os = None

    def __str__(self):
        return f"Computer [CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}, OS: {self.os}]"

# Abstract Builder
class ComputerBuilder:
    def set_cpu(self, cpu):
        pass

    def set_ram(self, ram):
        pass

    def set_storage(self, storage):
        pass

    def set_gpu(self, gpu):
        pass

    def set_os(self, os):
        pass

    def build(self):
        pass

# Concrete Builder
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_os(self, os):
        self.computer.os = os
        return self

    def build(self):
        return self.computer

# Director (Optional)
class Director:
    @staticmethod
    def construct_gaming_pc(builder):
        return (builder.set_cpu("Intel i9")
                .set_ram("32GB")
                .set_storage("1TB SSD")
                .set_gpu("NVIDIA RTX 4090")
                .set_os("Windows 11")
                .build())

# Client Code
if __name__ == "__main__":
    builder = GamingComputerBuilder()

    # Using Builder Directly
    custom_pc = (builder.set_cpu("AMD Ryzen 9")
                      .set_ram("16GB")
                      .set_storage("512GB SSD")
                      .set_gpu("AMD Radeon RX 7900")
                      .set_os("Linux")
                      .build())
    print(custom_pc)

    # Using Director to Construct a Predefined Gaming PC
    gaming_pc = Director.construct_gaming_pc(GamingComputerBuilder())
    print(gaming_pc)
