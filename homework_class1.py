import random

#1
def task_1():
    keys_for_dict = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dict_1 = {x: x*x for x in keys_for_dict}
    return dict_1
print("1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key): ", task_1())

#2
def task_2():
    list_21 = [x*2 for x in range(1, 51)]
    return list_21
print("2) результирующий массив только четные числа.: ", task_2())

#3
def task_3():
    string_31 = "some random string"
    new_string_31 = ""
    con = "bcdfghjklmnpqrstvwxz"
    vow = "aeiouy"
    for char in string_31:
        if char in con:
            char = random.choice(vow)
        new_string_31 += char
    return new_string_31
print("3)Заменить в произвольной строке согласные буквы на гласные: ", task_3())

#4
def task_4():
    mas = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    #4.1
    mas_41 = list(set(mas))
    #4.2
    mas_42 = sorted(mas_41, reverse = True)
    #4.3
    #4.4
    mas_44 = list(mas)
    mas_44.reverse()
    return mas, mas_41, mas_42[0:3], mas.index(min(mas)), mas_44
print("4) mas = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1] ", task_4()[0])
print("4.1) убрать из него повторяющиеся элементы: ", task_4()[1])
print("4.2) вывести 3 наибольших числа из исходного массива: ", task_4()[2])
print("4.3) вывести индекс минимального элемента массива: ", task_4()[3])
print("4.4) вывести исходный массив в обратном порядке: ", task_4()[4])

#5
def task_5():
    dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
    list_51 = (dict.keys(dict_one))
    list_52 = (dict.keys(dict_two))
    result = list(set(list_51) & set(list_52))
    return result
print("5) Найти общие ключи в двух словарях:  ", task_5())
