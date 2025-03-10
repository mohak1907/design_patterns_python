"""
Adapter design pattern
Description - 
    Name itself suggest that this pattern has a nature of
    adapting to each others. Adapter method provides multiple
    interfaces for different classes so they can understand or
    adapt each other even they are actually incompatible
    
    We have many real life examples for this pattern.
    Writing at console or in a file.
"""

# Adaptee
class ConsoleWriter:
    '''
    console writer class
    '''
    def pprint(self, text):
        '''console write method'''
        print(text)


# Target Interface
class FileWriter:
    '''file writter class'''
    def write(self, text, file_name='output.txt'):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)


# Adapter
class WriteAdapter:
    '''Adapter Main class'''
    def __init__(self, writer)-> None:
        self.writer = writer
    
    def write(self, *args):
        '''Adapter generic write method'''
        if isinstance(self.writer, ConsoleWriter):
            self.writer.pprint(*args)
        elif isinstance(self.writer, FileWriter):
            self.writer.write(*args)


if __name__ == '__main__':
    console_writer = ConsoleWriter()
    file_writer = FileWriter()

    adapter_1 = WriteAdapter(console_writer)
    adapter_2 = WriteAdapter(file_writer)

    adapter_1.write("Writing to Console")
    adapter_2.write("Writing to file", "adapter.txt")
    