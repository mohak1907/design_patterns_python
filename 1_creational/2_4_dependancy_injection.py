"""
When to Use This Advanced Factory Pattern?
    1. When You Have External Dependencies
        (e.g., database connections, logging services, API clients)
    2. When Object Creation is Complex
        (e.g., multiple dependencies injected dynamically)
    3. When You Want High Testability
        DI makes unit testing much easier by replacing real services with mocks.
    4. When You Want Loose Coupling
        The client does not depend on concrete classes, making the system modular.
"""


from abc import ABC, abstractmethod

# Step 1: Define an abstract base class (Interface)
class Notification(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

# Step 2: Create a Logger Service (Dependency)
class Logger:
    def log(self, message: str):
        print(f"[LOG]: {message}")

# Step 3: Create Concrete Classes Implementing Notification Interface
class EmailNotification(Notification):
    def __init__(self, logger: Logger):
        self.logger = logger

    def notify(self, message: str):
        self.logger.log("Email notification sent")
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def __init__(self, logger: Logger):
        self.logger = logger

    def notify(self, message: str):
        self.logger.log("SMS notification sent")
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def __init__(self, logger: Logger):
        self.logger = logger

    def notify(self, message: str):
        self.logger.log("Push notification sent")
        print(f"Sending Push Notification: {message}")

# Step 4: Implement the Factory with Dependency Injection
class NotificationFactory:
    def __init__(self, logger: Logger):
        self.logger = logger  # Inject dependency

    def create_notification(self, notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification(self.logger)
        elif notification_type == "sms":
            return SMSNotification(self.logger)
        elif notification_type == "push":
            return PushNotification(self.logger)
        else:
            raise ValueError("Unknown notification type")
        

def testing():

    class MockLogger:
        def log(self, message: str):
            pass  # Does nothing (simulating a logger without side effects)

    # Test the Factory with Mock Logger
    mock_logger = MockLogger()
    factory = NotificationFactory(mock_logger)

    # Create and test an Email Notification
    email_notification = factory.create_notification("email")
    email_notification.notify("Test Message")


# Step 5: Client Code using the Factory
if __name__ == "__main__":
    logger_service = Logger()  # Dependency

    # Create the Factory with Logger Dependency
    factory = NotificationFactory(logger_service)

    # Get Notification Type from User
    notification_type = input("Enter notification type (email/sms/push): ").strip().lower()

    try:
        notification = factory.create_notification(notification_type)
        notification.notify("Hello! This is a test message.")
    except ValueError as e:
        print(f"Error: {e}")

    # testing()