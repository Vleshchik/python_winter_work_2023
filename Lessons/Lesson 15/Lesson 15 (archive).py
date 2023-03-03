#1
lst = [1, 2, [11, 22, [111, 222, [1111, 2222, 3333], 333, 444, [555, 666]], 33], 3]
res = []
def list_pos(lst):
    for i in lst:
        if type(i) == list:
            list_pos(i)
        else:
            res.append(i)
    return res
print(list_pos(lst))
#2
import re
string = 'числа 99, 72, 81 и 999 делятся на 9'
print(re.findall(r' \d{2},', string))
#3
import re
string = '123, 100, 199, 12222, 99, 200'
regex = r"\b1\d{2}\b"
print(re.findall(regex, string))
#4
import re
string = 'Косой косой cкосил траву на косе'
regex = r"\b\w+\b"
regex2 = r"\b\w*[Кк]ос\w+\b"
print(re.findall(regex, string))
print(re.findall(regex2, string))
#5
import re
string = 'aaa.aaa bbb.bbb 333-333-3333 A123BC78 A123BC198 A123BC128 A123BC80'
regex = r"\b\w{3}\.\w{3}\b"
regex2 = r"\d{3}-\d{3}-\d{4}"
regex3 = r"\b[A-Z]\d{3}[A-Z]{2}1?[7,9]8\b"
print(re.findall(regex, string))
print(re.findall(regex2, string))
print(re.findall(regex3, string))
#6
import re
text = 'Java самый популярный язык программирования в 2023 году'
res = re.sub(r'Java', r'Python', text)
print(res)
#7
import re
text = 'Java самый популярный язык программирования в 2023 году'
res, n = re.subn(r'Java', r'Python', text)
print(res, n)
#8
import re
text = '(095)-4325 095-3333 33-(095)-33'
res= re.sub(r'\(095\)', r'(812)', text)
print(res)