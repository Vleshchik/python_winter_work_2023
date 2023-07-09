import itertools
lst = []
lst2 = []
n = str(input())
for x in itertools.permutations(['a','a','b','b']):
    lst.append(''.join(x))
l = set(lst)
for x in itertools.permutations(n):
    lst2.append(''.join(x))
l2 = set(lst2)
print(l)
print(l2)