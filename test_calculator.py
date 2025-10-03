import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-2, 4), -8)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333, places=4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
