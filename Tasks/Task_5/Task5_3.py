n = int(input())
fib = [1, 1]
for i in range(2, n):
    f = fib[i - 1] + fib[i - 2]
    fib.append(f)
print(fib)
