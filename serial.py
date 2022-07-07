"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.rst=start

    def __repr__(self):
        '''show representation. '''
        return f"<SerialGeenerator start = {self.start} next = {self.rst}>"
    
    def generate(self):
        '''
         return the next sequential number
        '''
        self.rst = self.rst + 1
        return self.rst - 1
    
    def reset(self):
        ''' reset the number back to the original start number'''
        self.rst = self.start

