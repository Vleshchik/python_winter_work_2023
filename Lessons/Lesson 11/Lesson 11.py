import calendar
year = 2023 #int(input('Введите год: '))
tue_lst = []
free_count = 0
for month in range(1, 13):
    count = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        if calendar.weekday(year, month, day) == 3:
            count += 1
            if count == 3:
                tue = list[str(year), str(month), str(day)]
                tue_lst.append(tue)
                free_count += 1
print(free_count)
print(tue_lst)



