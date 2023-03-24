def comparison(x, y):
    count = 0
    if abs(len(x)-len(y)) > 1:
        return False
    elif abs(len(x)-len(y)) == 1:
        if x in y or y in x:
            return True
        else:
            return False
    else:
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
    if count <= 1:
        return True
    else:
        return False

print(comparison('abc', 'abc')) #True
print(comparison('abc', 'abcd')) #True
print(comparison('bc', 'abc')) #True
print(comparison('axc', 'abc')) #True
print(comparison('abc', 'acb')) #False
print(comparison('abc', 'a')) #False
print(comparison('', '  ')) #False
print(comparison('abc', 'ax')) #False