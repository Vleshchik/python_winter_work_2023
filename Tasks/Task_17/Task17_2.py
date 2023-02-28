def uppercase_list_decorator(fu):
    def wrapper():
        original_r = fu()
        modified_r = original_r.upper().split()
        return list(modified_r)
    return wrapper
@uppercase_list_decorator
def text():
    str = input() #Косой косой косил волос на откосе
    return str
print(text())