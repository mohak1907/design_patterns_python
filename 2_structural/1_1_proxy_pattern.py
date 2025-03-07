"""
Proxy Design Pattern-
It is a structural design pattern, which provides interface for different kind of objects like
networking objects, files with heavy memory size, images, etc
There is one real method, and then a proxy method is created from the same interface class, which acts
as a proxy method(example: just like a proxy server).
"""

from abc import ABCMeta, abstractmethod

class AbstractCmd(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, command):
        pass

class RealCmd(AbstractCmd):

    def execute(self, command):
        print(f"{command} command executed.")


class ProxyCmd(AbstractCmd):

    def __init__(self, user):
        self.is_authorized = False
        if user == "admin":
            self.is_authorized = True
        self.executor = RealCmd()
        self.restricted_commands = ['rm', 'mv']

    def execute(self, command):
        if self.is_authorized:
            self.executor.execute(command)
        else:
            if any([command.strip().startswith(cmd)
                    for cmd in self.restricted_commands]):
                raise Exception(f"{command} command is not allowed for non-admin users.")
            else:
                self.executor.execute(command)


if __name__ == '__main__':
    admin_executor = ProxyCmd("admin")
    other_executor = ProxyCmd("other")
    try:
        admin_executor.execute("ls -la");
        admin_executor.execute("rm -rf /");
        print("\n")
        other_executor.execute("ls -la");
        other_executor.execute("rm -rf");
    except Exception as e:
        print("Error:",e)