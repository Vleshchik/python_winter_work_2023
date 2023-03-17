import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
con = psycopg2.connect(
    database = 'postgres',
    user= 'postgres',
    password='3267',
    host='127.0.0.1',
    port='5432'
)
cur = con.cursor()
cur.execute('SELECT * FROM book1')
rows = cur.fetchall()
d = {'price':[], 'amount':[]}
for i in rows:
    d['price'].append(i[3])
    d['amount'].append(i[4])


df = pd.DataFrame(d)

con.close()

df.plot('price','amount', kind = 'scatter')
plt.show()