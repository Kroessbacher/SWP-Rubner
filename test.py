import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

def geheim(a, b, c=42,**data):
    print(data)

geheim(1,3, c=42)

def geheim2(a, b, /, *, c=5):
    pass

def aussen():
    def innen():
        pass

    c=5
    return c

def myFunction(a,b,c,**kwargs):
    return print(a,b,c, kwargs)

myDict = {'b':2,'a':1,'c':3,'d':4}
myFunction(**myDict)