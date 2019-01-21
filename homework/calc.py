class Calculator:
    """Performs basic calculator functions such as add, subtract, divide,
    multiply, and clear.
    Attributes:
        a: An integer or float passed in to start off calculations.
    """
    def __init__(self, a = None):
        """Return a new Calculator object. 'a' is passed in when initialized,
        and 'b' is passed in when specific functions are called."""
        if a is None:
            self.a = 0.0
        else:
            self.a = a

    def add(self, b):
        """Adds two numbers, a and b."""
        self.a += float(b)

    def sub(self, b):
        """Subtracts b from a."""
        self.a -= float(b)

    def mul(self, b):
        """Multiplies b and a."""
        self.a *= float(b)

    def div(self, b):
        """Divides a by b."""
        try:
            self.a /= float(b)
        except ZeroDivisionError as err:
            print(err)

    def clr(self):
        """Reassigns a to zero."""
        self.a = 0.0

    def result(self):
        """Returns value of a."""
        return self.a
