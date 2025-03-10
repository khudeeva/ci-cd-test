def longest_word(sentence):
    if not isinstance(sentence, str):
        return "Ошибка: не строка"
    
    words = sentence.split()
    if not words:
        return "Ошибка: пустая строка"
    
    return max(words, key=len)