import re
# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.


# удаление только четных слов
def task_1_1():
    with open("text_file_1.txt", "r") as file_task1, open("text_file_5.txt", "w") as file_result:
        result = []
        for i in file_task1:
            cnt = 0
            for words in i[:-1].split():
                if 3 <= len(words.strip()) <= 5:
                    cnt += 1
                    if cnt % 2 == 0:
                        continue
                result.append(words.strip())
            file_result.write(' '.join(result)+'\n')
            print(result)
            result.clear()


task_1_1()


# удаление только четного количества слов
def task_1_2():
    result = []
    with open("text_file_1.txt", "r") as file_task1, open("text_file_5.txt", "w") as file_result:
        for i in file_task1:
            cnt = 0
            for words in i[:-1].split():
                if 3 <= len(words.strip()) <= 5:
                    cnt += 1
            cnt = cnt if cnt % 2 == 0 else cnt - 1
            for words in i[:-1].split():
                if 3 <= len(words.strip()) <= 5 and cnt:
                    cnt -= 1
                    continue
                result.append(words.strip())
            file_result.write(' '.join(result)+'\n')
            print(result)
            result.clear()


task_1_2()

# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.

my_file = open("text_file_2.txt", "r")
my_file_result = open("text_file_3.txt", "w")


def task_2():
    data = my_file.readlines()
    result = list()
    for line in data:
        match = re.findall("(C\w+:.+|K\w+:.+)", line)
        result += match
    string_result = "\n".join(result)
    return string_result


my_file_result.write(task_2())
my_file.close()
my_file_result.close()

# Задача-3 - не обязательна к выполнению
# Написать декоратор который будет подавлять ошибки возникающие в теле вашей функции.
# Например ваша функция может иметь вид
# def my_func():
#    raise ValueError("some text error")

# Задача-4 - не обязательна к выполнению
# Написать декоратор c аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш декоратор вы должны передать ему в качестве аргумента
