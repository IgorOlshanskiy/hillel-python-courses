import re
import json
import os

# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)


class IpAddress(object):

    def __init__(self, ip_list):
        self._ip_list = ip_list

    def get_ip(self):
        return self._ip_list

    def reverse(self):
        return list(reversed(self._ip_list))

    def without__first_octets(self):
        temp_str = ", ".join(self._ip_list)
        match = re.findall(r"(?:\d{2}.)(\d{2}.\d{2}.\d{2})", temp_str)
        return match

    def only_last_octets(self):
        temp_str = ", ".join(self._ip_list)
        match = re.findall(r"(?:\d{2}.\d{2}.\d{2}.)(\d{2})", temp_str)
        return match


ip = IpAddress(ip_list=["10.11.12.13", "77.88.99.11"])
print("Получить список IP адресов: ", ip.get_ip())
print("Получить список IP адресов в развернутом виде:", ip.reverse())
print("Получить список IP адресов без первых октетов: ", ip.without__first_octets())
print("Получить список последних октетов IP адресов: ", ip.only_last_octets())


# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить относительный путь к файлу
# 5) Получить абсолютный путь к файлу

class JsonWork(object):

    def __init__(self, path, path1, path2):
        self._path = path
        self._path1 = path1
        self._path2 = path2
        self._data = None

    def readfile(self):
        try:
            with open(self._path, "r") as f:
                self._data = json.loads(f.read())
                return self._data
        except FileNotFoundError as e:
            print(e)

    def writefile(self):
        try:
            with open(self._path2, "w") as f1:
                json.dump(self._data, f1, indent=4)
        except FileNotFoundError as e:
            print(e)

    def concatenation(self):
        try:
            with open(self._path, "r") as f, open(self._path1, "r") as f1, open(self._path2, "w") as f3:
                data = json.loads(f.read())
                data1 = json.loads(f1.read())
                data_result = dict(data, **data1)
                json.dump(data_result, f3, indent=4)
        except FileNotFoundError as e:
            print(e)

    def absolute(self):
        return os.path.abspath(self._path)

    def relative(self):
        return os.path.basename(self._path)


js = JsonWork(path="json_example.json", path1="json_example_1.json", path2="json_example_w.json")
print("Чтение из файла: ", js.readfile())
print("Запись в файл, json_example.json", js.writefile())
print("Объединение данных из файлов в новый файл, json_example.json", js.concatenation())
print("Получить относительный путь к файлу: ", js.relative())
print("Получить абсолютный путь к файлу: ", js.absolute())

# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.


class Switch(object):

    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

# unit_name

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, new_unit_name):
        self._unit_name = new_unit_name

    @unit_name.deleter
    def unit_name(self):
        del self._unit_name

# mac_address

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, new_mac_address):
        self._mac_address = new_mac_address

    @mac_address.deleter
    def mac_address(self):
        del self._mac_address

# ip_address

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, new_ip_address):
        self._ip_address = new_ip_address

    @ip_address.deleter
    def ip_address(self):
        del self._ip_address

# login

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @login.deleter
    def login(self):
        del self._login

# password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @password.deleter
    def password(self):
        del self._password


sw = Switch(unit_name="Asus", mac_address="10.11.12.13", ip_address="15.16.17.18",
            login="iolshanskiy", password="12345")
sw.new_unit_name = "Utify"
sw.new_mac_address = "10.11.12.13"
sw.new_ip_address = "15.16.17.18"
sw.new_login = "Igor"
sw.new_password = "*****"
print(sw.unit_name, sw.mac_address, sw.ip_address, sw.login, sw.password)
print(sw.new_unit_name, sw.new_mac_address, sw.new_ip_address, sw.new_login, sw.new_password)
