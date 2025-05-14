import os
import json
from calculator import (
    add, subtract, multiply, divide, power, capitalize_word, remove_duplicates,
    save_list_to_csv, save_json, load_json, sort_list, remove_spaces,
    text_lower, return_modul, number_max, text_upper, min_number, add_element
)

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Ошибка: деление на ноль"

def test_large_numbers():
    assert add(1000000000, 2000000000) == 3000000000
    assert multiply(100000, 1000) == 100000000

def test_divide_negative():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5

def test_zero_operations():
    assert add(0, 10) == 10
    assert subtract(0, 10) == -10
    assert multiply(0, 100) == 0

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_capitalize_word():
    assert capitalize_word("hello") == "Hello"
    assert capitalize_word("WORLD") == "World"
    assert capitalize_word("123") == "123"
    assert capitalize_word(100) == "Ошибка: не строка"

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates(["apple", "banana", "apple"]) == ["apple", "banana"]
    assert remove_duplicates([]) == []
    assert remove_duplicates(123) == "Ошибка: не список"

def test_save_list_to_csv():
    filename = "test_output.csv"
    test_data = ["apple", "banana", "cherry"]
    save_list_to_csv(filename, test_data)
    with open(filename, "r") as file:
        content = file.read().strip()
    assert content == "apple,banana,cherry"
    os.remove(filename)

def test_json_operations():
    filename = "test.json"
    test_data = {"name": "Alice", "age": 25}
    save_json(filename, test_data)
    result = load_json(filename)
    assert result == test_data
    os.remove(filename)

def test_sort_list():
    assert sort_list([3, 2, 1]) == [1, 2, 3]
    assert sort_list(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]
    assert sort_list([5]) == [5]
    assert sort_list([]) == []
    assert sort_list("hello") == "Ошибка: не список"

def test_remove_spaces():
    assert remove_spaces("   Hello   world   ") == "Hello world"
    assert remove_spaces("Python    is    great") == "Python is great"
    assert remove_spaces("   OnlyStartSpaces") == "OnlyStartSpaces"
    assert remove_spaces("NoSpaces") == "NoSpaces"
    assert remove_spaces("   ") == ""
    assert remove_spaces(123) == "Ошибка: не строка"

def test_text_lower():
    assert text_lower("HELLO WORLD") == "hello world"
    assert text_lower("Hello world") == "hello world"
    assert text_lower("hello world") == "hello world"
    assert text_lower("") == ""
    assert text_lower("123") == "123"
    assert text_lower(123) == "Ошибка: не строка"

def test_return_modul():
    assert return_modul(-10) == 10
    assert return_modul(-5) == 5
    assert return_modul(0) == 0
    assert return_modul(5) == 5
    assert return_modul("Hello") == "Ошибка: не число"
    assert return_modul("") == "Ошибка: не число"

def test_number_max():
    assert number_max([3, 6, 8]) == 8
    assert number_max([1, 10, 7]) == 10
    assert number_max([1, 0, 1]) == 1
    assert number_max([0, 0, 0]) == 0
    assert number_max([-3, -6, -8]) == -3
    assert number_max([]) == "Ошибка: пустой список"
    assert number_max("123") == "Ошибка: не список"

def test_text_upper():
    assert text_upper("hello") == "HELLO"
    assert text_upper("hello world") == "HELLO WORLD"
    assert text_upper("Hello") == "HELLO"
    assert text_upper("") == ""
    assert text_upper(123) == "Ошибка: не строка"

def test_min_number():
    assert min_number([1, 2, 3]) == 1
    assert min_number([-1, -2, -3]) == -3
    assert min_number([1, 1, 1]) == 1
    assert min_number([]) == "Ошибка: пустой список"
    assert min_number("123") == "Ошибка: не список"

def test_add_element():
    assert add_element([1, 2]) == [1, 2, "новый элемент"]
    assert add_element(["a", "b"]) == ["a", "b", "новый элемент"]
    assert add_element([]) == ["новый элемент"]
    assert add_element(123) == "Ошибка: не список"
