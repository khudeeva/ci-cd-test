import unittest
from count_vowels import count_vowels
    
class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("Привет"), 2)
        self.assertEqual(count_vowels("Это проверка"), 5)
        self.assertEqual(count_vowels("Кот"), 1)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("123"), 0)
        self.assertEqual(count_vowels(123), "Ошибка: не строка")

if __name__ == "__main__":
    unittest.main()