from functools import wraps
from typing import Callable

data = [20, "hi", 3.14]


def decorator(filter_type: str):
    def decorator_inner(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list):
                if filter_type == 'str':
                    result = [item for item in result if not isinstance(item, str)]
                elif filter_type == 'int':
                    result = [item for item in result if not isinstance(item, int)]
                elif filter_type == 'float':
                    result = [item for item in result if not isinstance(item, float)]
            return result
        return wrapper
    return decorator_inner


@decorator('str')
def get_data_str() -> list:
    return data


@decorator('int')
def get_data_int() -> list:
    return data


@decorator('float')
def get_data_float() -> list:
    return data


@decorator('please delete nothing')
def get_data() -> list:
    return data


print(get_data_str())
print(get_data_int())
print(get_data_float())
print(get_data())
