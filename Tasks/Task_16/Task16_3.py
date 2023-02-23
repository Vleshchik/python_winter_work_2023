def titlecase_decorator(fu):
    def wrapper():
        original_string = fu()
        modified_string = original_string.title()
        return modified_string
    return wrapper
@titlecase_decorator
def text():
    s = input()
    return s
print(text())