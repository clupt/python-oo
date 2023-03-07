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

    def __init__(self, start=100):
        """ Create serial number generator from number passed """
        self.start = start
        self.current_num = start
        self.counter = 0

    def __repr__(self):
        return f"""<Serial Generator start={self.start},
        current_num={self.current_num}, and counter={self.counter}"""

    def generate(self):
        """ Returns the next sequential number """
        self.counter += 1
        if self.counter > 1:
            self.current_num += 1
            return self.current_num
        else:
            return self.current_num

    def reset(self):
        """ Resets start to the original start value and counter to 0"""
        self.current_num = self.start
        self.counter = 0
