def tri_2(n):
    print('*' * n)
    if n > 2:
        tri_2(n - 1)
    elif n == 2:
        print('*' * (n - 1))
    print('*' * n)
tri_2(int(input()))