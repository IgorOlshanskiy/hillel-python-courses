
import re

# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить


class EmailDescriptor:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        if re.findall(r"(\w+@\w+\.\w+)", value):
            self.value = value
        else:
            raise RuntimeError("Incorrect email format: {}".format(value))
        print("Task_1 valid email format:", value)


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"
# my_class.email = "novalidemail" # Raised Exception


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


class NotClass():
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)
print("Task_2: ", c == b)

x = NotClass()
y = NotClass()
print("Task_2: ", x == y)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:

    def __get__(self, instance, owner):
        return instance._number
        #return self.value

    def __set__(self, instance, value):
        instance._number = value
        #self.value = value


class Data:
    number = IngegerField()

    # def __init__(self):
    #     self.number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

print("Task_3: ", data_row.number)
print("Task_3: ", new_data_row.number)
print("Task_3: ", data_row.number != new_data_row.number)
