dct = {1:1, 2:2, 3:{2:22, 3:{4:111, 2:222, 1:{0:1111, 1:2222, 2:3333}, 3:333}, 1:11}, 6:22} #элемент 111 в 1:111 не выведется, так как после него в словаре есть элемент 1:333
x = 1
res = []
def dct_sort(dct):
    for k, v in dct.items():
        if k == x:
            res.append(v)
        if type(v) == dict:
            dct_sort(v)
    return res
print(dct_sort(dct))
