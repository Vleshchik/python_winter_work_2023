import itertools
l = [1, 2, 3, 4, 5]
homework = dict(itertools.zip_longest(*[iter(l)] * 1, fillvalue="not solved"))

print(homework)