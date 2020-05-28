def decorator(func):
    """decorator docstring"""
    def inner_function(*args, **kwargs):
        """inner function docstring """
        print( func.__name__ + "was called")
        return func(*args, **kwargs)
    return inner_function

@decorator
def foobar(x):
    """foobar docstring"""
    return x**2

print( foobar.__name__)
print( foobar.__doc__)