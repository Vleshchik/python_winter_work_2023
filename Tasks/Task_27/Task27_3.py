
def count(l, res = []):
    for i in l:
        if type(i) == list:
            res.append(1)
            count(i)
        else:
            res.append(i)
    return len(res)
print(count([]))
#print(count([1, 2, 3]))
#print(count([1, 2, [3]]))
#print(count([1,2,[3,4, [5]]]))