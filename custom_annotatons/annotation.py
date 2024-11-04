from functools import wraps

# Define the decorator
def greet_decorator(func):
    @wraps(func)
    def wrapper(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError(f"Expected a string, but got {type(name).__name__}")
        return func(f"Hello, {name}!")
    return wrapper

# Define a function to use the decorator with
@greet_decorator
def greet(name: str) -> str:
    return name
