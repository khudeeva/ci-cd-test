import unittest
from is_prime import is_prime  # Импортируем функцию

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(17), True)
        self.assertEqual(is_prime(20), False)
        self.assertEqual(is_prime(1), "Ошибка: число должно быть больше 1")
        self.assertEqual(is_prime(-7), "Ошибка: число должно быть больше 1")
        self.assertEqual(is_prime(123.5), "Ошибка: не число")
        self.assertEqual(is_prime("текст"), "Ошибка: не число")

if __name__ == "__main__":
    unittest.main()
