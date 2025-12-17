from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = 0
    parameters = []

    def wrapper(*args, **kwargs) -> Any:
        nonlocal cached_data
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
