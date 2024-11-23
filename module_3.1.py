# Задача "Счётчик вызовов":
# Отследить сколько раз вызывалась та или иная функция.
calls = 0  # создали переменную счетчик


def count_calls():  # функция подсчета вызовов
    global calls
    calls += 1


def string_info(string):  # функция строка-->кортеж (длина,верхний регистр,нижний регистр)
    str_info = str(string)
    info = (len(str_info), str_info.upper(), str_info.lower()) # кортеж
    count_calls()  # вызываем функцию счетчика
    return info  # выводим результат работы функции строка-->кортеж


def is_contains(string, list_compare):  # функция строка+список сравнение
    compare = bool  # введем переменную для результата,ну и чтоб не ругался PyCharm(!!!)
    string = str(string).lower()  # переводим символы строки в нижний регистр
    list_compare = list(list_compare)  # вводим переменную для списка
    count_calls()  # фызываем функцию счетчика
    for i in range(len(list_compare)):
        if str(list_compare[i]).lower() == string:  # сравниваем элемегт списка и строку
            compare = True
            break
        else:
            compare = False
        continue
    return compare #


print(string_info("UNIVERSITY"))
print(string_info("URBAN"))
print(is_contains("DDT", ["Kino", "ARIYA", "NAUTILUS"]))  # нет совпадений
print(is_contains("People", ["Hour", "WEEK", "DAY", "PeOpLe"]))  # совпадение

print(calls)
