def count_vowels(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0

    for letter in text:
        if letter.lower() in vowels:
            count += 1
        
    return count
    