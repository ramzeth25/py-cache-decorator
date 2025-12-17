from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    parameters = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in parameters:
            cached_data = func(*args, **kwargs)
            parameters[key] = cached_data
            print("Calculating new result")
            return cached_data
        else:
            print("Getting from cache")
            return parameters[key]
    return wrapper
