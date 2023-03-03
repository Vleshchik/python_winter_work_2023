import calendar
year = int(input())
print(*[(day, month, year) for month in range (1, 13) for day in range(1, calendar.monthrange(year, month)[1] + 1)])