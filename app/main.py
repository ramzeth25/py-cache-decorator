from typing import Callable, Any


def cache(func: Callable) -> Callable:
    parameters = {}

    def wrapper(*args, **kwargs) -> Any:
        if (args, tuple(sorted(kwargs.items()))) not in parameters:
            cached_data = func(*args, **kwargs)
            parameters[(args, tuple(sorted(kwargs.items())))] = cached_data
            print("Calculating new result")
            return cached_data
        else:
            print("Getting from cache")
            return parameters[(args, tuple(sorted(kwargs.items())))]
    return wrapper
