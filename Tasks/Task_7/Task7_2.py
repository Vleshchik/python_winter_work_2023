str = str(input()) #abcdefghijklmnopqrstuvwxyz
n = int(input())
string = list(str)
def code(string, n):
    for i in range(len(string)):
        if 65 <= ord(string[i]) <= 90 or 97 <= ord(string[i]) <= 122:
            if ord(string[i]) + n > 90 and ord(string[i]) + n < 97:
                j = ord(string[i]) + n - 90
                nl = chr(ord('Z') - 26 + j)
                string[i] = nl
            elif ord(string[i]) + n > 122:
                j = ord(string[i]) + n - 122
                nl = chr(ord('z') - 26 + j)
                string[i] = nl
            else:
                nl = chr(ord(string[i]) + n)
                string[i] = nl
        else:
            continue
    return ''.join(string)
print(code(string, n))