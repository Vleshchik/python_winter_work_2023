import pandas as pd
n_lst = int(input('Введите количетсво строк:'))
lst = []
max_c = 0
sum_n = 0
for i in range(n_lst):
    st = []
    n_num = int(input(f'Введите количество чисел в строке №{i + 1}: '))
    for j in range(n_num):
        n = int(input(f'Введите число №{j + 1}: '))
        st.append(n)
        if max_c < len(st):
            max_c = len(st)
    lst.append(st)
df = pd.DataFrame(lst, columns=[i for i in range(max_c)])
for i in df.columns:
    sum_n += df[i].sum()
print(sum_n)