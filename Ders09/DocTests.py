import doctest
import unittest

class Calculator:
    """
    >>> c = Calculator()
    >>> c.add(2, 3)
    5
    >>> c.subtract(2, 3)
    -1
    >>> c.divide(2, 3)
    0
    >>> c.multiply(2, 3)
    6
    """
    def add(self, a, b):
        """
        >>> c = Calculator()
        >>> c.add(6, 9)
        15
        """
        return a+b

    def subtract(self, a, b):
        """
        >>> c = Calculator()
        >>> c.subtract(20, 2)
        18
        """
        return a-b

    def divide(self, a, b):
        """
        >>> c = Calculator()
        >>> c.divide(-9, -2)
        4
        """
        return a//b

    def multiply(self, a, b):
        """
        >>> c = Calculator()
        >>> c.multiply(-6, -2)
        12
        """
        return a*b


def suite():
    my_suite = unittest.TestSuite()
    temp_module = __import__("Ders09")
    my_suite.addTest(doctest.DocTestSuite(temp_module.DocTests))
    return my_suite


def run_tests():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())


if __name__ == '__main__':
    doctest.testmod()