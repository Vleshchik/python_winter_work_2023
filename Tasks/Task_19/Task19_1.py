import itertools
lst = []
for x in itertools.combinations([50,100,200,500,1000,5000], 3):
    lst.append(sum(x))
print(lst)