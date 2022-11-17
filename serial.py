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

    def __init__(self, start=0):
        """if no value passed as start, the start value in __init__() defaults to 0
            start refers to the argument in the __init__()
            self.start is the instance method. For example, when we call serial = SerialGenerator(start=100), we create an instance object that has start:100 as a property pair.
        """
        self.start = start
        # self.start =100
        self.next = start
        # self.next =100

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        self.next = self.next + 1
        # self.next = 100 + 1 = 101
        return self.next - 1

    def reset(self):
        self.next = self.start
