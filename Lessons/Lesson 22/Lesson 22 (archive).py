#1
import matplotlib.pyplot as plt
import pandas as pd
x, y = [], []
for i in range(100):
    x.append(i)
    y.append(i ** 2)
df = pd.DataFrame({'x':x, 'y':y})
df.plot('x','y', kind = 'scatter')
plt.show()
#2
import matplotlib
import pandas as pd
df = pd.DataFrame({'a':[1,2,3,4,5,6,7,8,9], 'b':[1,1,1,2,2,2,3,3,3]})
print(df.plot())
#3