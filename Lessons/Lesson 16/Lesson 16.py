def lowercase_decorator(fu):
    def wrapper():
        original_r = fu()
        modified_r = original_r.lower()
        return modified_r
    return wrapper
@lowercase_decorator
def text():
    s = input()
    return s
print(text())
