# Цель: применить знания о рекурсии в решении задачи.
# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number
# и подсчитывает произведение цифр этого числа.

def get_multiplied_digits(n):
    n = int(n)  # убираем нули в начале числа
    str_number = str(n)
    first = int(str_number[0])
    #i = len(str_number) # введена для просмотра изменений в отладчике
    while str_number.endswith('0'):  # отсекаем нули в конце числа
        str_number = str_number[:len(str_number) - 1] # срез списка, если последний элемент "0"
    if len(str_number) > 1: # проверка условия, не закончились ли цифры числа
        return first * get_multiplied_digits(int(str_number[1:])) #  рекурсия, срез первой цифры числа
    else:
        return first

result = get_multiplied_digits(4020300)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
result3 = get_multiplied_digits("000402030") # ввел третий вариант, посмотреть как убираются первые нули
print(result3)

