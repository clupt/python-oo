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
        self.start = start - 1
        self.original_start = start - 1

    def __repr__(self):
        return f"""<Serial Generator start={self.start}
            and original_start={self.original_start}"""

    def generate(self):
        """ Returns the next sequential number """
        self.start += 1
        return self.start

    def reset(self):
        """ Resets start to the original start value"""
        self.start = self.original_start
