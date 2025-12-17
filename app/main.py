from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = 0
    parameters = []
    def wrapper(*args, **kwargs):
        nonlocal cached_data, parameters
        if args and args not in parameters:
            parameters.append(args)
            cached_data = func(*args, **kwargs)
            print("Calculating new result")
            return cached_data
        elif kwargs and kwargs not in parameters:
            parameters.append(kwargs)
            cached_data = func(*args, **kwargs)
            print("Calculating new result")
            return cached_data
        else:
            print("Getting from cache")
            return cached_data

    return wrapper



@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)


