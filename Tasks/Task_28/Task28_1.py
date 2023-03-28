def inversion(l):
    count = 0
    for i in range(len(l)-1):
        for j in range(i, len(l)-1):
            if l[i] > l[j+1]:
                count += 1
    return count
print(inversion([1,2,3,4,5]))
print(inversion([5,4,3,2,1]))
print(inversion([1,1,1,1,1]))
print(inversion([1,2,3,2,1]))