import datetime
from collections import OrderedDict
cache = None


def lru_cache(_func=None, *, cached=False, max_size=128):
    global cache
    cache = OrderedDict()

    def wrapper(func):
        if not cached:
            return func

        def inner_wrapper(*args):
            if len(cache) == max_size:
                last_updated = list(cache.keys())[0]
                del cache[last_updated]
            func_data = (func, args)
            if func_data in cache:
                return
            cache[func_data] = func(*args)
            cache.move_to_end(func_data)
        return inner_wrapper
    if _func:
        return wrapper(_func)
    return wrapper


def timeit(func):
    def wrapper(*args):
        start = datetime.datetime.now()
        result = func(*args)
        end = datetime.datetime.now()
        print("Время выполнения: " + str(end - start))
        return result
    return wrapper
