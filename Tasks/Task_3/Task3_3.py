str = str(input())
marks = '''!@#$%^&*(){}[]\|;:'",.<>/?'''
for x in str:
    if x in marks:
        str = str.replace(x, "")
print(str)
s = str.split()
mx = len(s[0])
lst = [s[0]]
max_word = s[0]
for i in range(len(s)):
    if mx < len(s[i]):
        lst.clear()
        mx = len(s[i])
        max_word = s[i]
        lst.append(max_word)
    elif i != 0 and mx == len(s[i]):
        lst.append(s[i])
print(lst)
