import functools
#fp
def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@memoize
def your_function(x, y):

    print("Calculating...")
    return x + y

result1 = your_function(3, 4)
print(result1)

result2 = your_function(3, 4
print(result2)
