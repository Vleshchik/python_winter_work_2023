import psycopg2
import pandas as pd
con = psycopg2.connect(
    database = 'postgres',
    user= 'postgres',
    password='3267',
    host='127.0.0.1',
    port='5432'
)
cur = con.cursor()
#cur.execute('SELECT * FROM book1')
#cur.execute("insert into test values (11, 'Федотов', 600, 'C#')")
#con.commit()
cur.execute('select * from test')
rows = cur.fetchall()
d = {'id':[], 'name':[], 'salary':[], 'language':[]}
for i in rows:
    print(i)
    d['id'].append(i[0])
    d['name'].append(i[1])
    d['salary'].append(i[2])
    d['language'].append(i[3])
print(d)
df = pd.DataFrame(d)
print(df)
con.close()
