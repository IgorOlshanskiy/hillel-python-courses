import contextlib
import os
import time

# class suppress(object):
#
#     def __init__(self, suppressed):
#
#         self.suppressed = suppressed
#
#     def __enter__(self):
#
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#
#         return exc_type is not None and issubclass(exc_type, self.suppressed)
#
#
# with suppress(KeyError):
#
#     raise KeyError
#
# #################
#
# import contextlib
#
#
#
# @contextlib.contextmanager
#
# def context():
#
#     print('enter to our block')
#
#     try:
#
#         yield {}
#
#     except RuntimeError as e:
#
#         print("error: {}".format(e))
#
#     finally:
#
#         print("out of block")
#
#
#
#
#
# with context() as fp:
#
#     print("do_something")
#
#
# class cd:
#
#     def __init__(self, path):
#
#         self.path = path
#
#         self.saved_cwd = None
#
#     def __enter__(self):
#
#         self.saved_cwd = os.getcwd()
#
#         os.chdir(self.path)
#
#     def __exit__(self, *exc_info):
#
#         os.chdir(self.saved_cwd)
#
#
# print("CURR_DIR = {}".format(os.getcwd()))
#
# with cd("F:\Education"):
#
#     print("CHDIR = {}".format(os.getcwd()))
#
# print("CURR_DIR = {}".format(os.getcwd()))
#
# ##########################################################
#
# class Hello:
#
#     def __enter__(self):
#
#         print('enter to our block')
#
#         return 1
#
#
#
#     def __exit__(self, exp_type, exp_value, traceback):
#
#         print("out of block")
#
#
# with Hello() as s:
#
#     print(s)
#
#     print("something")


# Задача-1
# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.

class MyException(Exception):
    pass


class cd(object):

    def __init__(self, path, flag_ex, exception):
        self.path = path
        self.flag_ex = flag_ex
        self.exception = exception
        self.saved_cwd = None

    def __enter__(self):
        if self.flag_ex and self.exception is not None:
            print("Task_1: Error suppressed")
            self.saved_cwd = os.getcwd()
            os.chdir(self.path)
        else:
            raise self.exception

    def __exit__(self, *args):
        os.chdir(self.saved_cwd)


with cd(path="F:\\", flag_ex=True, exception=MyException):
    print("Task_1: CHDIR = {}".format(os.getcwd()))


# Задача -2
# Описать задачу выше но уже с использованием @contexmanager

@contextlib.contextmanager
def context(path, flag_ex, exception):
    print("Task_2_step1: CURDIR = {}".format(os.getcwd()))
    if flag_ex and exception is not None:
        print("Task_2_step2: Error suppressed")
        os.chdir(path)
    else:
        raise exception
    try:
        yield {}
    except RuntimeError as e:
        print("Task_2_step1_1: error: {}".format(e))
    finally:
        print("Task_2_step2: CHRDIR = {}".format(os.getcwd()))


with context("F:\\", True, MyException) as fp:
    pass


# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполняния блока инструкций

class Task_3(object):

    def __enter__(self):
        self.time_start = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        time_finish = time.time()
        result = time_finish - self.time_start
        return print("Task_3: ", result)


with Task_3() as h:
    list_time = [x * 2 for x in range(10000000)]
