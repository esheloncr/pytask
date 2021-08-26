import datetime
from functools import update_wrapper
from typing import Callable, Any


def cache(use_cache=True) -> Callable:
    """
    Improvised cache function that caches a result of functions and their arguments
    @param use_cache: flag to use cache
    @type use_cache: bool
    @return: wrapped function
    """
    def decorated_function(func: Callable) -> Callable:
        wrapper = _cache(func, use_cache)
        return update_wrapper(wrapper, func)
    return decorated_function


def _cache(func: Callable, use_cache=True) -> Callable:
    """
    Internal function that hash function arguments and check it into cached_args list.
    If them not in list func result will be calculated and append into cached_function dictionary where
    key is arguments hash and value is result of function
    @param func: users wrapped function
    @param use_cache: parameter sent from previous function
    @return: wrapped function
    """
    cached_function = {}
    cached_args = []

    def wrapper(*args, **kwargs) -> Any:
        arguments = hash(frozenset([*args, frozenset(kwargs)]))
        if arguments in cached_args and use_cache:
            return cached_function[arguments]
        result = func(*args, **kwargs)
        cached_function[arguments] = result
        cached_args.append(arguments)
        return result

    wrapper.cached_function = cached_function
    return wrapper


def timeit(func: Callable) -> Callable:
    def wrapper(*args) -> Any:
        start = datetime.datetime.now()
        result = func(*args)
        end = datetime.datetime.now()
        print("Lead time: " + str(end - start))
        return result
    return wrapper
