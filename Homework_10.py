

# Исходный список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Список для простых чисел
primes = []
# Список для непростых чисел
not_primes = []

for number in numbers:
    # 1 не является простым числом
    if number < 2:
        continue
    # Поумоланию счетаем все числа простыми
    is_prime = True
    
    # Перебираем числа 2 до number
    for i in range(2, number):
       # Проверяем делимость если нашли делитель, число не простое
       if number % i == 0:
            is_prime = False  
            break
       
    # Записываем число в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)