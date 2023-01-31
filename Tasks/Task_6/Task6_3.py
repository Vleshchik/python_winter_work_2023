str = str(input().lower())
lst = list(str)
lst_n = '''1234567890'''
lst_s = '''!@#$%^&*(){}[]\|;:'",.<>/?_-=+'''
lst_l = '''qwertyuiopasdfghjklzxcvbnm'''
def uni_let(lst):
    set_l = set()
    set_n = set()
    set_s = set()
    for i in lst:
        if i in lst_n:
            set_n = set_n.union(i)
        elif i in lst_l:
            set_l = set_l.union(i)
        else:
            set_s = set_s.union(i)
    str_s = sorted(set_s)
    str_l = sorted(set_l)
    str_n = sorted(set_n)
    str_s = ' '.join(str_s)
    str_l = ' '.join(str_l)
    str_n = ' '.join(str_n)
    return f'{str_l}\n {str_n}\n {str_s}'
print(uni_let(lst))