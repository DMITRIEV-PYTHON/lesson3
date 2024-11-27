# Домашнее задание по уроку "Распаковка позиционных параметров".
# Цель задания: Освоить создание функций с параметрами по умолчанию
# и практику вызова этих функций  с различным количеством аргументов.

def print_params(a=1, b='String', c=True):  # создали функцию
    print(a, b, c)


print_params(2, 5)
print_params()
print_params("URBAN", "Dima", "MIDDLE")
print_params(b=25)  # подставляет во второй параметр число 25
print_params(c=[1, 2, 3])  # подставляет в третий параметр список

value_list = [True, 23, "Junior"]
value_dict = {'a': 1, 'b': "COMP", 'c': False}
print_params(value_list)  # список встал на место первого параметра
print_params(*value_list)  # список распаковался, значения встали на места параметров
print_params(value_dict)  # словарь встал на место первого параметра
print_params(**value_dict)  # словарь распаковался, значения встали на места параметров

value_list_2 = [True, 23]
print_params(*value_list_2,42)