#1
import numpy as np
x = np.array([2, 7, 7, 8, 8, 6, 8, 7, 6, 7])
condition = x < np.percentile(x, 25)
print(np.percentile(x, 25))
print(x[condition])
#2
import numpy as np
n = int(input('Введите n: '))
x = list(range(1, n * n + 1))
print(x)
x = np.array(x)
y = x.reshape((n, n))
print(y)
print(np.median(y))
print(np.median(y, axis = 0))
print(np.median(y, axis = 1))
#3
import pandas as pd
df1 = pd.DataFrame([[1, 'Bob', 'Builder'], [2, 'Sally', 'Baker'], [3, 'Skott', 'Candle Stick Maker']], columns=['id', 'name','occupation'])
print(df1)
df2 = pd.DataFrame({'country':['Kaz', 'Rus', 'Bel', 'Ukr'], 'population':[17, 143, 9, 45], 'square':[1, 2, 3, 4]})
print(df2)
