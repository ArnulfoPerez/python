from functools import wraps

def wrapped_decorator(func):
    """wrapped decorator docstring"""
    @wraps(func)
    def inner_function(*args, **kwargs):
        """inner function docstring """
        print (func.__name__ + " was called")
        return func(*args, **kwargs)
    return inner_function


@wrapped_decorator
def foobar(x):
    """foobar docstring"""
    return x**2

print (foobar.__name__)
print( foobar.__doc__)

foobar(4)