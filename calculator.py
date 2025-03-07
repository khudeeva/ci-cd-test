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

