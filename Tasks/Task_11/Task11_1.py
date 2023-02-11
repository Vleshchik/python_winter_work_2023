import calendar
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'ru')
year = int(input('Введите год: '))
tue_lst = []
for month in range(1, 13):
    count = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        if calendar.weekday(year, month, day) == 3:
            count += 1
            if count == 3:
                tue = date(year, month, day)
                tue_lst.append(tue.strftime('%d %B %Y'))
print(f'В {year} году билеты в Эрмитаж бесплатны в следующие даты: ')
for i in tue_lst:
    print(i)
