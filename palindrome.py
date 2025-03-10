def is_palindrome(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]