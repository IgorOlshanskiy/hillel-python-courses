# 1)Дан массив из словарей 
# 1.1) отсортировать массив из словарей по значению ключа ‘age' 
# 1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :
# result = {
#    'Kiev':  [{'name': 'Viktor', 'age': 30 },
#               {'name': 'Andrey', 'age': 34}],
#    'Dnepr': [{'name': 'Maksim', 'age': 20 },
#               {'name': 'Artem', 'age': 50}],
#    'Lviv': [{'name': 'Vladimir', 'age': 32 },
#              {'name': 'Dmitriy', 'age': 21}]}

from itertools import groupby
from operator import itemgetter
from collections import Counter

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]


def task_1_1():
    data.sort(key=lambda k: k["age"], )
    return data[:]


print("1.1) отсортировать массив из словарей по значению ключа ‘age' : ", task_1_1())


# Задание 1.2 не осилил всё на что хватило сил:
def task_1_2():
    data1 = [
        {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
        {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
        {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
        {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
        {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
        {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
    data1.sort(key=itemgetter('city'))
    return data1


print("Задание 1.2 не осилил всё на что хватило сил:", task_1_2())


# =======================================================
# 2) У вас есть последовательность строк.
# Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:
# def most_frequent(list_var):
# your code is here
#    return
# most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'

def task_2():
    string = ['a', 'a', 'bi', 'bi', 'bi', 'ggg', 'ggg', 'ggg', 'ggg']
    max_occur = Counter(string)
    return max_occur.most_common(1)


print("2) Наиболее часто встречающуюся строку в последовательности:", task_2())


# =======================================================
# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

def task_3():
    num = 1023405
    num_list = [int(x) for x in str(num)]
    list1 = sorted(num_list)
    prod = 1
    for i in list1:
        if i != 0:
            prod *= i
    return prod


print("3) Подсчитать произведение всех цифр в этом числе, за исключением нулей: ", task_3())


# =======================================================
# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.


def task_4():
    n = 5
    num_list = [1, 2, 3, 4, 5]
    if n >= len(num_list):
        return "-1"
    else:
        a = num_list.pop(n)
        return a ** n


print("4) Найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1: ",
      task_4())


# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.
def task_5():
    str = "hello 1 one two three four 15 world"
    cnt = 0
    for i in str.split():
        if i.isalpha():
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 0


print("5) Есть ли в исходной строке три слова подряд: ", task_5())
