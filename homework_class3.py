import re


# Задача-1
#
# Дан произвольный текст. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в тексте.
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohh.",
# если мы соберем все заглавные буквы, то получим сообщение "HELLO".


def task_1():
    string = "How are you? Eh, ok. Low or Lower? Ohh."
    new_tupl = []
    for i in string:
        if i.isupper():
            new_tupl += i
    string_result = "".join(new_tupl)
    return string_result


print("Задача-1:", task_1())


# Задача-2
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.
# mas = [0, 1, 2, 3, 4, 5] = 0 + 2 + 4 = 6 * 5 = 30


def task2():
    mas = [0, 1, 2, 3, 4, 5]
    res = 0
    for i in mas:
        if i % 2 == 0:
            res += i * mas[-1]
    return res


print("Задача-2:", task2())

# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все
def task_3():
    string = ",.\ Ho'w are you? Eh, ok."
    match = re.search("[A-Za-z']+", string)
    return match.group(0)


print("Задача-3:", task_3())
# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.


def task_4():
    string_new = "How are you"
    #    str_list = [x for x in string_new]
    str_list = list(string_new)
    str_list[-1], str_list[0] = str_list[0], str_list[-1]
    string_new = "".join(str_list)
    return string_new


print("Задача-4:", task_4())


# Задача-5
# Дан тапл(tuple), необходимо его конвертнуть в стринг.
# Например:
# ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's') == 'exercises


def task_5():
    tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
    string_tup = "".join(tup)
    return string_tup


print("Задача-5:", task_5())
