def isEven(value):
    return True if str(value)[-1] == '0' or str(value)[-1] == '2' or str(value)[-1] == '4' or str(value)[-1] == '6' or str(value)[-1] == '8' else False
print(isEven(3.2))