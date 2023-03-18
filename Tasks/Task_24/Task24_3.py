s = "(()) (( () () ) () )" # ")(()))" "(" "(()) (( () () ) () )" "()"
c = 0
for i in s:
    if c >= 0:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
    else:
        break
if c == 0:
    print(True)
else:
    print(False)