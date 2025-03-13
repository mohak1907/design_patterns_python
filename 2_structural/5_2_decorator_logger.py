"""
Advanced Decorator Design Pattern Example: Logging System
In this advanced example, we use the Decorator Pattern to create a flexible logging system that supports multiple
logging functionalities, such as:
    1. Console Logging
    2. File Logging
    3. Timestamped Logging
    4. Error Level Logging
    5. JSON Formatting for Logs
Instead of modifying the core logger, we dynamically enhance its functionality by wrapping it with different
decorators.

Advantages:
    ✅ Highly Flexible: New logging features can be added without modifying existing code.
    ✅ Composable: Any combination of decorators can be applied dynamically.
    ✅ Extensible: Easy to add more decorators (e.g., database logging, email alerts).

Disadvantages:
    ❌ Can Become Complex: Too many layers of decorators may make debugging harder.
    ❌ Execution Overhead: Each decorator adds a function call overhead.

Explanation:
    1. Component (Logger)
        Defines the log() method.
    2. Concrete Component (ConsoleLogger)
        Implements a simple console-based logger.
    3. Decorator (LoggerDecorator)
        Wraps another Logger object and forwards calls.
    4. Concrete Decorators
        TimestampLogger: Adds timestamps to logs.
        ErrorLevelLogger: Adds log levels (INFO, ERROR, DEBUG).
        FileLogger: Writes logs to a file while still logging to the console.
        JSONLogger: Formats logs as JSON.
    5. Client Code
        Starts with a basic console logger.
        Dynamically wraps it with decorators to add timestamps, error levels, file logging, and JSON formatting.
"""
from abc import ABC, abstractmethod
import datetime
import json

# Component Interface (Logger)
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Concrete Component (Basic Console Logger)
class ConsoleLogger(Logger):
    def log(self, message):
        print(message)

# Decorator (Base Wrapper)
class LoggerDecorator(Logger):
    def __init__(self, logger):
        self._logger = logger

    def log(self, message):
        self._logger.log(message)

# Concrete Decorator 1: Timestamp Logger
class TimestampLogger(LoggerDecorator):
    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().log(f"[{timestamp}] {message}")

# Concrete Decorator 2: Error Level Logger
class ErrorLevelLogger(LoggerDecorator):
    def __init__(self, logger, level="INFO"):
        super().__init__(logger)
        self.level = level

    def log(self, message):
        super().log(f"[{self.level}] {message}")

# Concrete Decorator 3: File Logger (Writes logs to a file)
class FileLogger(LoggerDecorator):
    def __init__(self, logger, filename="logfile.txt"):
        super().__init__(logger)
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as file:
            file.write(message + "\n")
        super().log(message)  # Also log to console

# Concrete Decorator 4: JSON Logger (Formats log messages as JSON)
class JSONLogger(LoggerDecorator):
    def log(self, message):
        log_entry = {"timestamp": datetime.datetime.now().isoformat(), "message": message}
        super().log(json.dumps(log_entry))

# Usage Example
if __name__ == "__main__":
    # Basic Logger
    logger = ConsoleLogger()
    logger.log("Basic log message")

    print("\n--- Enhanced Logging ---")
    
    # Logger with Timestamp
    logger = TimestampLogger(logger)
    logger.log("This log has a timestamp")

    # Logger with Error Level
    logger = ErrorLevelLogger(logger, "ERROR")
    logger.log("This is an error log")

    # Logger that writes to a file
    logger = FileLogger(logger)
    logger.log("This log is written to a file and console")

    # Logger with JSON format
    logger = JSONLogger(logger)
    logger.log("This log is formatted as JSON")
