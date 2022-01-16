import unittest

class Calculator:
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b

    def divide(self, a, b):
        return a//b

    def multiply(self, a, b):
        return a*b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()

    def test_sum(self):
        self.assertEqual(self.c.add(3, 5), 8, "Dogrusu 8")

    def test_subtract(self):
        self.assertEqual(self.c.subtract(3, 5), -2, "Dogrusu -2")

    def test_divide(self):
        self.assertEqual(self.c.divide(3, 5), 0, "Dogrusu 0")

    def test_multiply(self):
        self.assertEqual(self.c.multiply(3, 5), 15, "Dogrusu 15")

    def tearDown(self):
        pass


def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestCalculator('test_sum'))
    my_suite.addTest(TestCalculator('test_subtract'))
    my_suite.addTest(TestCalculator('test_divide'))
    my_suite.addTest(TestCalculator('test_multiply'))
    return my_suite


def run_tests():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())


if __name__ == '__main__':
    unittest.main()