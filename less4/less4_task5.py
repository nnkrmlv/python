from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, tuple(range(100, 1001, 2))))
