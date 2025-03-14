from abc import ABC, abstractmethod

# Command Interface
class BaseCommannd(ABC):
    '''
    Base command class
    '''

    @abstractmethod
    def execute(self):
        raise NotImplementedError("Please implement in subclass")

# Concrete Commands
class EMailCommand(BaseCommannd):
    '''
    Email Command class
    '''
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_email(self.data)

# Concrete Commands
class SMSCommand(object):
    '''
    Command class
    '''
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_sms(self.data)


# Receiver (The actual logic)
class NotificationService(object):
    '''
    Receiver class
    '''
    def send_email(self, data):
        print("Sending email", data)

    def send_sms(self, data):
        print("Sending short message", data)


# Invoker (Stores and executes commands)
class NotificationInvoker(object):
    '''
    Invoker class
    ''' 
    def __init__(self):
        self.notification_history = []

    def invoke(self, command):
        self.notification_history.append(command)
        command.execute()

if __name__ == "__main__":
    invoker = NotificationInvoker()
    receiver = NotificationService()
    invoker.invoke(EMailCommand(receiver, {"subject": "Test Email"}))
    invoker.invoke(SMSCommand(receiver, {"subject": "Test SMS"}))
    print(invoker.notification_history)