def count_n(n):
    return 1 if n // 10 == 0 else 1 + count_n(n // 10)
print(count_n(int(input())))