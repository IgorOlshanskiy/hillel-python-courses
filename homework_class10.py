# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем


def get_all_lines(file_list):
    lines = []
    for f in file_list:
        with open(f) as fd:
            for line in fd:
                if line not in lines:
                    lines.append(line)
                    yield line.strip()


for line in get_all_lines(["text_file_1.txt"]):
    print("Task_1: ", line)

# gen = get_all_lines(["text_file_1.txt"])
# next(gen)
# next(gen)
# next(gen)


# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```
# def coroutine(*args):
#     # your code here
#
#
# @coroutine
# def grep(*args):
# 	# your code here
#
#
# @coroutine
# def printer():
# 	# your code here
#
#
# @coroutine
# def dispenser(*args):
#     # your code here
#
#
# def follow(*args):
#     # your code here
# ```
#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#
# ```
# f_open = open('log.txt') # подключаемся к файлу
# follow(f_open,
#        # делегируем ивенты
#        dispenser([
#            grep('python', printer()), # отслеживаем
#            grep('is', printer()),     # заданные
#            grep('great', printer()),  # сигнатуры
#        ])
#        )
# ```
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
#
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
#
# Если все плохо - план Б лекция Дэвида Бизли
# [warning] решение там тоже есть :)
# https://www.dabeaz.com/coroutines/Coroutines.pdf


import time


def coroutine(func):
    def generator(*args, **kwargs):
        primed_func = func(*args, **kwargs)
        primed_func.__next__()
        return primed_func
    return generator


def follow(file, target):
    file.seek(0, 2)
    try:
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            target.send(line)
    except StopIteration:
        print("Pipeline Ended")


@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


@coroutine
def printer():
    try:
        while True:
            line = (yield)
            print("Task_2 ", line.strip())
    except GeneratorExit:
        print("Printer Pipeline Ended")


@coroutine
def dispenser(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)


if __name__ == '__main__':
    with open("text_file_1.txt", "r") as f:
        follow(f, dispenser([grep('python',printer()),
                            grep('is',printer()),
                            grep('great',printer())])
                )




#Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.
