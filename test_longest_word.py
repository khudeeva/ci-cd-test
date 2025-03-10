import unittest
from longest_word import longest_word  # Импортируем функцию

class TestLongestWord(unittest.TestCase):
    def test_longest_word(self):
        self.assertEqual(longest_word("Я люблю программирование"), "программирование")  
        self.assertEqual(longest_word("Котёнок играет с клубком"), "Котёнок")  
        self.assertEqual(longest_word(""), "Ошибка: пустая строка")  
        self.assertEqual(longest_word("Python нужно изучать много"), "изучать")  
        self.assertEqual(longest_word(12345), "Ошибка: не строка")  # Ошибка, если передано число  

if __name__ == "__main__":
    unittest.main()
