
def isomorph(x, y):
    if len(x) != len(y):
        return False
    else:
        for i in range(len(x)):
            for j in range(len(y)):
                if i != j and (x[i] == x[j] and y[i] != y[j]) or (x[i] != x[j] and y[i] == y[j]):
                    return False
    return True
print(isomorph('CBAABC', 'DEFFED'))
print(isomorph('XXX', 'YYY'))
print(isomorph('RAMBUNCTIOUSLY', 'THERMODYNAMICS'))
print(isomorph('AB', 'CC'))
print(isomorph('XXY', 'XYY'))
print(isomorph('ABAB', 'CD'))
print(isomorph('AB','CD'))