#1
d1 = {'apples':100, 'bananas': 333, 'pears': 300, 'oranges':300}
d2 = {'apples': 300, 'pears':200, 'raspberry': 777, 'pineaples': 12}
res = {}
for key in d1 | d2:
    res[key] = d1.get(key, 0) + d2.get(key, 0)
print(res)
#2
