import requests
from srange import srange
from func_utils import timeit
from collections import OrderedDict
from pprint import pprint

"""
This is an example of how modules work.
"""

# Comparing range and srange


@timeit
def compare_range():
    for i in range(10000000):
        pass


@timeit
def compare_srange():
    for i in srange(10000000):
        pass


"""
This is duplicate lru_cache with global cache to show how it works
"""
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


@lru_cache(cached=True, max_size=4)
def test_cache(url):
    encoding = requests.get(url).encoding
    return encoding


url_list = [
    "http://google.com",
    "http://habr.com",
    "https://httpbin.org/",
    "http://github.com",
    "http://facebook.com",
    "http://twitter.com",
    "http://youtube.com"
]


def main():
    print("range working time:")
    compare_range()
    print("srange working time:")
    compare_srange()
    for i in url_list:
        test_cache(i)
    print("lru_cache data")
    pprint(cache)
    test_cache(url_list[0])
    test_cache(url_list[2])
    print("lru_cache after update")
    pprint(cache)


if __name__ == '__main__':
    main()
