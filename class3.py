from functools import singledispatch
from timeit import default_timer as timer


# ПРАКТИКА ДЕКОРАТОРЫ:
#
# *Задача-1*
# Написать декоратор который выводит сообщение до вызова функции и после вызова функции
#
# *Задача-2*
# Написать декоратор который будет выводить время выполнения вашей функции
#
# *Задача-3*
# Написать декоратор который будет расширять(добавлять) аргументы к вашей функции.


def decorator(random_func):
    def wraps(*args):
        start = timer()
        print("Я декоратор")
        random_func(*args)
        random_func.x = 1
        print(random_func.__dict__)
        end = timer()
        print("Time taken:", end - start)

    return wraps


@decorator
def random_func():
    list_time = [x * 2 for x in range(1000000)]
    return list_time, print("функция")


print(random_func())


# *Задача -4*Написать декоратор который будет выполнять предпроверку типа аргумента
# который передается в вашу функцию. Если это int, тогда выполнить функцию и вывести результат,
# если это str(), тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))


@singledispatch
def new_func(x):
    print("Выполняю функция, у тебя int", x)
    return


@new_func.register(str)
def accept_func(x):
    print("raise ValueError('A very specific bad thing happened.')")


new_func("string")
