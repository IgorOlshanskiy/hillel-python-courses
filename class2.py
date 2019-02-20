# Если таблица продуктов на складе. Данные представлены в виде list of dicts
# Найти самые дорогие товары. Количество товаров,
# которые необходимо вывести будет передано в первом аргументе, данные по товарам будут переданы вторым аргументом.

data_list = [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 2200},
    {"name": "whiteboard", "price": 170}]


def bigger_price(limit, data):
    data.sort(key=lambda k: k["price"], reverse=True)
    return data[:limit]


print("result: ", bigger_price(2, data_list))


def number_diff(*args):
    args = (22, 33)
    return max(args) - min(args) if args else 0


print(number_diff())
