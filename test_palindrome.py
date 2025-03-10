import unittest
from palindrome import is_palindrome  # ✅ Добавили импорт

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("казак"), True)  
        self.assertEqual(is_palindrome("шалаш"), True)  
        self.assertEqual(is_palindrome("А роза упала на лапу Азора"), True)  
        self.assertEqual(is_palindrome("Привет"), False)  
        self.assertEqual(is_palindrome(""), True)  
        self.assertEqual(is_palindrome(123), "Ошибка: не строка")  

if __name__ == "__main__":
    unittest.main()
