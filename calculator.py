def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def capitalize_word(word):
    if not isinstance(word, str):
        return "Ошибка: не строка"
    return word.capitalize()

def remove_duplicates(lst):
    if not isinstance(lst, list):
        return "Ошибка: не список"
    return list(dict.fromkeys(lst))

import csv

def save_list_to_csv(filename, data):
    if not isinstance(data, list):
        return "Ошибка: не список"
    
    with open(filename, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerow(data)

import json

def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)

def sort_list(lst):
    if not isinstance(lst, list):
        return "Ошибка: не список"
    return sorted(lst)

def remove_spaces(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return " ".join(text.split())

def text_lower(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return text.lower()

def return_modul(number):
    if not isinstance(number, (int, float)):
        return "Ошибка: не число"
    return abs(number)

def number_max(lst):
    if not isinstance(lst, list):
        return "Ошибка: не список"
  
    if not lst:
        return "Ошибка: пустой список"
    
    return max(lst)

def text_upper(text):
    if not isinstance(text, str):
       return "Ошибка: не строка"
    
    return text.upper()

def min_number(lst):
    if not isinstance(lst, list):
        return "Ошибка: не список"
    
    if not lst:
        return "Ошибка: пустой список"
    
    return min(lst)

def add_element(lst):
    if not isinstance(lst, list):
        return "Ошибка: не список"
    
    lst.append("новый элемент")
    return lst
