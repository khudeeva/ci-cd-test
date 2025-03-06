import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), "Ошибка: деление на ноль")

    def test_large_numbers(self):
        self.assertEqual(add(1000000000, 2000000000), 3000000000)
        self.assertEqual(multiply(100000, 1000), 100000000)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_zero_operations(self):
        self.assertEqual(add(0, 10), 10)
        self.assertEqual(subtract(0, 10), -10)
        self.assertEqual(multiply(0, 100), 0)

if __name__ == '__main__':
    unittest.main()
