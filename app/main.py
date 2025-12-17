from typing import Callable, Any


def cache(func: Callable) -> Callable:
    parameters = {}

    def wrapper(*args, **kwargs) -> Any:
        if f"{args}, {kwargs}" not in parameters:
            cached_data = func(*args, **kwargs)
            parameters[f"{args}, {kwargs}"] = cached_data
            print("Calculating new result")
            return cached_data
        else:
            print("Getting from cache")
            return parameters[f"{args}, {kwargs}"]
    return wrapper
