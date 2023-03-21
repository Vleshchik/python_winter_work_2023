def CamelStyle(s):
    s = s.title().split()
    return ''.join(s)
w = input() #camel case word
print(CamelStyle(w))