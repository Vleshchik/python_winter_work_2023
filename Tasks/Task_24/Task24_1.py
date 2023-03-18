l = [1, 4, 21, 3, 43, 15, 10, 494, 45]
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)