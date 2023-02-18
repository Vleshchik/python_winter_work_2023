def sum_n(n):
    return n if n // 10 == 0 else n % 10 + sum_n(n // 10)
print(sum_n(int(input())))