
def isomorph(x, y):
    b = False
    if len(x) == len(y):
        for i in range(len(x)):
            for j in range(len(y)):
                if i != j and x[i] == x[j] and y[i] == y[j]:
                    b = True
    return print(b)
isomorph('CBAABC', 'DEFFED')
isomorph('XXX', 'YYY')
isomorph('RAMBUNCTIOUSLY', 'THERMODYNAMICS')
isomorph('AB', 'CC')
isomorph('XXY', 'XYY')
isomorph('ABAB', 'CD')