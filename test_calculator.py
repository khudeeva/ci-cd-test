import unittest
import os
import json
from calculator import add, subtract, multiply, divide, power, capitalize_word, remove_duplicates, save_list_to_csv, save_json, load_json, sort_list, remove_spaces, text_lower

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
    
    def test_power(self):
        self.assertEqual(power(2, 3), 8)  
        self.assertEqual(power(5, 0), 1)

    def test_capitalize_word(self):
        self.assertEqual(capitalize_word("hello"), "Hello")
        self.assertEqual(capitalize_word("WORLD"), "World")
        self.assertEqual(capitalize_word("123"), "123")
        self.assertEqual(capitalize_word(100), "Ошибка: не строка")
   
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates(["apple", "banana", "apple"]), ["apple", "banana"])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates(123), "Ошибка: не список")
 
    import os

    def test_save_list_to_csv(self):
        filename = "test_output.csv"
        test_data = ["apple", "banana", "cherry"]

        save_list_to_csv(filename, test_data)

        with open(filename, "r") as file:
            content = file.read().strip()

        self.assertEqual(content, "apple,banana,cherry")

        os.remove(filename)
    
    def test_json_operations(self):
        filename = "test.json"
        test_data = {"name": "Alice", "age": 25}

        save_json(filename, test_data)
        result = load_json(filename)

        self.assertEqual(result, test_data)

        os.remove(filename)
def test_sort_list(self):
    self.assertEqual(sort_list([3, 2, 1]), [1, 2, 3])
    self.assertEqual(sort_list(["banana", "apple", "cherry"]), ["apple", "banana", "cherry"])
    self.assertEqual(sort_list([5]), [5])
    self.assertEqual(sort_list([]), [])
    self.assertEqual(sort_list("hello"), "Ошибка: не список")

def test_remove_spaces(self):
    self.assertEqual(remove_spaces("   Hello   world   "), "Hello world")
    self.assertEqual(remove_spaces("Python    is    great"), "Python is great")
    self.assertEqual(remove_spaces("   OnlyStartSpaces"), "OnlyStartSpaces")
    self.assertEqual(remove_spaces("NoSpaces"), "NoSpaces")
    self.assertEqual(remove_spaces("   "), "")
    self.assertEqual(remove_spaces("123"), "Ошибка: не строка")

def test_text_lower(self):
    self.assertEqual(text_lower("HELLO WORLD"), "hello world")
    self.assertEqual(text_lower("Hello world"), "hello world")
    self.assertEqual(text_lower("hello world"), "hello world")
    self.assertEqual(text_lower(""), "")
    self.assertEqual(text_lower("123"), "123")
    self.assertEqual(text_lower(123), "Ошибка: не строка")


if __name__ == '__main__':
    unittest.main()
