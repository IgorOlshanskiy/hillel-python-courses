# LRU (least recently used) — это алгоритм, при котором вытесняются значения, которые дольше всего не запрашивались.
# Соответственно, необходимо хранить время последнего запроса к значению. И как только число закэшированных значений
# превосходит N необходимо вытеснить из кеша значение, которое дольше всего не запрашивалось.
#
#
# Задача - 1
# Создать декоратор lru_cache(подобный тому который реализован в Python).
#
# Задача-2
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_info  - статистика использования вашего кеша(например: сколько раз вычислялась ваша функция,
# а сколько раз значение было взято из кеша, сколько места свободно в кеше)
#
# Задача-3
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_clear - очищает кеш
#
# Пример обращения к служебному методу декоратора

# def decorator(my_func):
#      def wrapper():
#            my_func()
#
#      def cache_clear():
#            pass
#
#      wrapper.cache_clear = cache_clear
#      return wrapper
#
# @decorator
# def my_func():
#       pass
#
#
# my_func.cache_clear()

# def key_construct(args, kwargs):
#     key = args
#     if kwargs:
#         key += tuple(sorted(kwargs.items()))
#
#     return key
import collections
import functools


def lru_cache(maxsize=3):
    """"LRU cache decorator function"""

    def decorating_function(func):
        cache = collections.OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args
            # key = key_construct(args, kwargs)

            # try:
            #     result = cache.pop(key)
            #     wrapper.hits += 1
            # except KeyError:
            #     result = func(*args, **kwargs)
            #     wrapper.misses += 1
            if key in cache:
                result = cache.pop(key)
                wrapper.hits += 1
            else:
                result = func(*args, **kwargs)
                wrapper.misses += 1

                if len(cache) >= maxsize:
                    cache.popitem()

            cache[key] = result

            return result

        def cache_info():
            """LRU cache statistics"""
            print({
                'cache': dict(cache),
                'hits': wrapper.hits,
                'misses': wrapper.misses

            })

        def cache_clear():
            """Clear the cache and cache statistics"""

            cache.clear()
            wrapper.hits = wrapper.misses = 0

        wrapper.hits = wrapper.misses = 0
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    return decorating_function


@lru_cache()
def main(a, b):
    return a + b


main(10, 20)
main(10, 20)
main(30, 40)
main.cache_info()
