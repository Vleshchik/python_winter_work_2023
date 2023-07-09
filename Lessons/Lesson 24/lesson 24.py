j = lambda a: int(''.join(sorted(map(str, a), reverse=True)))
print(j([7, 71, 72])) # это не правильно