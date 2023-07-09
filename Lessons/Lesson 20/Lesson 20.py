import pandas as pd
df = pd.DataFrame({'Год':[2001, 2002, 2003, 2004, 2005], 'Товар':['A', 'B', 'C', 'D', 'E'], 'Шт':[10, 20, 30, 40, 50], 'Цена':[100, 50, 30, 20, 5]})
print(df)
df['Итого'] = df['Цена']*df['Шт']
print(df)
c1 = df['Цена'] == 50
c2 = df['Цена'] == 30
print(df[c1 | c2])
for i in df.index:
    for j in df.columns:
        print(df.loc[i, j], end = ' ')
    print()