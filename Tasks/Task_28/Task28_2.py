def hemming(x, y):
    return len([i for i in range(len(x)) if x[i] != y[i]])
print(hemming('abc', 'abc'))
print(hemming('abc', 'abd'))
print(hemming('abc', 'xyz'))