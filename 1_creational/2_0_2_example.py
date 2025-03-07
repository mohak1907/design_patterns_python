from abc import ABC, abstractmethod

# Step 1: Define an abstract base class (interface)
class Notification(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

# Step 2: Create concrete classes implementing the interface
class EmailNotification(Notification):
    def notify(self, message: str):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def notify(self, message: str):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def notify(self, message: str):
        print(f"Sending Push Notification: {message}")

# Step 3: Implement Factory Method
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Unknown notification type")

# Step 4: Client Code using the Factory
if __name__ == "__main__":
    notification_type = input("Enter notification type (email/sms/push): ").strip().lower()
    notification = NotificationFactory.create_notification(notification_type)
    notification.notify("Hello! This is a test message.")
