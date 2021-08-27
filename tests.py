from srange import srange
from pytest import mark
from func_utils import cache

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


data_for_srange = [
    [50, 50],
    [90, 90],
    [-20, 0],
    [110, 110],
    [-999, 0],
]


@mark.parametrize("a, result", data_for_srange)
def test_srange_len_result(a, result):
    test = srange(a)
    assert len(test) == result


data_for_count_test = [
    [20, 40, 22, 1],
    [1, 999, 1001, 0],
    [-50, 2, 1, 1],
    [20, -15, 0, 0],
    [200, 332, 333, 0],
]


@mark.parametrize("a, b, value, result", data_for_count_test)
def test_srange_count(a, b, value, result):
    test = srange(a, b)
    test_value = test.count(value)
    assert test_value == result


data_for_index_test = [
    [20, 50, 24, 4],
    [0, 100, 50, 50],
    [32, 33, 32, 0],
    [0, 20, 0, 0],
    [100, 222, 222, 122],
]


@mark.parametrize("a, b, value, result", data_for_index_test)
def test_srange_index(a, b, value, result):
    test = srange(a, b)
    try:
        test_index = test.index(value)
        assert test_index == result
    except Exception as e:
        assert e.__class__ == IndexError
