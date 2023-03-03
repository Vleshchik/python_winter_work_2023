x = int(input())
y = int(input())
a = x + y
print(a)
b = x - y
print(b)
c = x * y
print(c)
d = x / y
print(d)
e = x // y
print(e)
f = x ** y
print(f)
# Следующими командами мы разделим пары числе на большие и меньшие
if a > b:
    max1_1 = a
    min1_1 = b
else:
    max1_1 = b
    min1_1 = a
if c > d:
    max1_2 = c
    min1_2 = d
else:
    max1_2 = d
    min1_2 = c
if e > b:
    max1_3 = e
    min1_3 = f
else:
    max1_3 = f
    min1_3 = e
#Сейчас мы найдем наибольшее число
if max1_1 > max1_2:
    if max1_1 > max1_3:
        min2_1 = max1_2
        min2_2 = max1_3
        print("Наибольшее число", max1_1)
    else:
        min2_1 = max1_2
        min2_2 = max1_1
        print("Наибольшее число", max1_3)
elif max1_2 > max1_3:
    min2_1 = max1_1
    min2_2 = max1_3
    print("Наибольшее число", max1_2)
# Сейчас мы найдем наибольшее из наименьших чисел (из тех, что отсеялись в первых парах сравнения)
if min1_1 > min1_2:
    if min1_1 > min1_3:
        maxmin_1 = min1_1
    else:
        maxmin_1 = min1_3
elif max1_2 > max1_3:
    maxmin_1 = min1_2
# Теперь мы знаем три числа: максимальное из минимальных и два отсеявшихся минимальных и можем узнать, который из них наибольший и тем самым найдем второе по величине число
if maxmin_1 > min2_1:
    if maxmin_1 > min2_2:
        print("Второе по величине число", maxmin_1)
    else:
        print("Второе по величине число", min2_2)
elif min2_1 > min2_2:
    print("Второе по величине число", min2_1)
# Так как использовался принцип турнирной сетки, то для простоты сравниваемым числам по итогу присваивались новые имена