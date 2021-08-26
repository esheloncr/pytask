from srange import srange
from pytest import mark
from random import randint, choice
from func_utils import cache


def generate_step():
    a = randint(1, 25)
    return a


def generate_data():
    a = [[randint(-1000, 0), randint(0, 1000)] for i in range(100)]  # range(100) - count of tests
    j = None
    for i in range(len(a)):
        c, b = a[i]
        for j in range(c, b):
            pass
        a[i].append(j)
    return a


def generate_data_2():
    a = [[randint(-1000, 0), randint(0, 1000), generate_step()] for i in range(100)]
    j = None
    for i in range(len(a)):
        b, c, d = a[i]
        for j in range(b, c, d):
            pass
        a[i].append(j)
    return a


def generate_data_3():
    a = [[randint(500, 1000), randint(0, 500), generate_step()] for i in range(100)]
    j = None
    for i in range(len(a)):
        b, c, d = a[i]
        for j in range(b, c, d):
            pass
        a[i].append(j)
    return a


def generate_data_4():
    a = [[randint(0, 1000), randint(0, 1000)] for i in range(200)]
    j = None
    for i in range(len(a)):
        b, c = a[i]
        d = range(b).count(c)
        a[i].append(d)
    return a


def generate_data_5():
    arr = []
    for i in range(1000):
        arr.append(i)
    return arr


data = generate_data()
data2 = generate_data_2()
data3 = generate_data_3()
data4 = generate_data_4()
data5 = generate_data_5()


def test_one_parameter():
    arr = []
    for i in srange(1000):
        arr.append(i)
    assert arr == data5


@mark.parametrize("a, b, result", data)
def test_two_params(a, b, result):
    i = None
    for i in srange(a, b):
        pass
    assert i == result


@mark.parametrize("a, b, c, result", data2)
def test_positive_step(a, b, c, result):
    i = None
    for i in srange(a, b, c):
        pass
    assert i == result


@mark.parametrize("a, b, c, result", data3)
def test_negative_step(a, b, c, result):
    i = None
    for i in srange(a, b, c):
        pass
    assert i == result


@mark.parametrize("a, b, result", data4)
def test_count(a, b, result):
    value = srange(a).count(b)
    assert value == result


def test_index():
    a = [i for i in range(1000)]
    for i in srange(1000):
        random_int = choice(a)
        b = range(1000).index(random_int)
        c = srange(1000).index(random_int)
        assert c == b


test_data_for_cache_function = [
    [5, 7, 12],
    [1, 20, 21],
    [12, 20, 32],
    [49, 21, 70],
    [333, 333, 666],
]


@mark.parametrize("a, b, result", test_data_for_cache_function)
def test_cache_function_result(a, b, result):
    @cache(use_cache=True)
    def improvised_sum(a, b):
        return a + b

    res = improvised_sum(a, b)
    assert res == result
    assert res in improvised_sum.cached_function.values()


def test_cache_function_name():
    @cache(use_cache=True)
    def improvised_name():
        return
    assert improvised_name.__name__ == "improvised_name"
