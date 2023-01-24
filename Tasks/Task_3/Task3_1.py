i = 1
n = 0
lst = []
while i > 0:
    i = int(input())
    if i == 0:
        break
    else:
        lst.append(i)
        n = n + i
mid = n // len(lst)
print(lst)
print("Количество работников на предприятии: ", len(lst))
print("Средняя зарпдата на предприятии: ", mid)