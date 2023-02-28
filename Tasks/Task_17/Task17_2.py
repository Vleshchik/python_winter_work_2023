def uppercase_list_decorator(fu):
    def wrapper(*args, **kwargs):
        res = []
        original_str = fu(*args, **kwargs)
        for i in args:
            if type(i) == str:
                res.append(i.upper())
        for i in kwargs:
            if type(kwargs[i]) == str:
                res.append(kwargs[i].upper())
        return res
    return wrapper
@uppercase_list_decorator
def text(*args, **kwargs):
    return
print(text('qwerty', 's', 'abc', a = 3, b = 'def'))