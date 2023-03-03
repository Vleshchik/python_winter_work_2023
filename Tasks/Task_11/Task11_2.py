import csv
import openpyxl
from openpyxl import Workbook
table = []
with open('task11_2.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    for row in rows:
        table.append(row)
title = table[0]
table.remove(table[0])
table_sort = sorted(table, key= lambda x: (x[3], x[1], x[2]))
sum_salary = 0
for i in table:
    sum_salary += int(i[4])
wb = openpyxl.load_workbook('task11_2.xlsx')
ws = wb.active
ws.append(title)
for i in table_sort:
    ws.append(i)
ws.append(['',"Итого",'','', sum_salary])
wb.save('task11_2.xlsx')