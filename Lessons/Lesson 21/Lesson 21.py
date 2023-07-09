import pandas as pd
import random
import openpyxl
df = pd.DataFrame(columns= ['Год', 'Товар', "Шт", 'Цена'], index= range(20))
x = 0
for i in range(2001, 2006):
    for j in ['A', 'B', 'C', 'D']:
        k = [10, 20, 30, 40, 50][random.randint(0, 4)]
        m = [100, 50, 30, 20, 5][random.randint(0, 4)]
        df.iloc[x] = [i, j, k, m]
        x += 1
df['Итого'] = df['Цена'] * df['Шт']
print(df)
#df.to_excel('test2.xlsx')
#print(df[df['Товар'].isin(['A', 'B'])][['Итого', 'Год']])
#print(df.sort_values('Итого', ascending= False).head(4))
#print(df.groupby('Год').Итого.sum())
#print(df.groupby('Товар').Итого.sum())
#print(df[df['Итого'] == df['Итого'].max()])
#print(df[1:len(df):2])
me = df['Цена'].mean()
print(me)
print(df[df['Цена'] < me])
print(df.groupby('Товар').Итого.sum().sort_values(ascending= False).head(2))
