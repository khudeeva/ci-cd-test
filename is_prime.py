def is_prime(num):
    if not isinstance(num, (int)):  # Проверяем, число ли это
        return "Ошибка: не число"
    
    if num < 2:  # Простые числа начинаются с 2
        return "Ошибка: число должно быть больше 1"
    
    for i in range(2, int(num ** 0.5) + 1):  # Проверяем делители от 2 до √num
        if num % i == 0:  # Если число делится без остатка → не простое
            return False

    return True  # Если не делится ни на одно число → простое
