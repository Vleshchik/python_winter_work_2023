import re
text = '(095)-4325 095-3333 33-(095)-33'
res= re.sub(r'\(095\)', r'(812)', text)
print(res)
