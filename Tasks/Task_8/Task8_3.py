s = input().split() # abab xx aaaaaaa abcbab dhijro bbcc ss dddd
print(s)
print(str(sorted(s, key = lambda x: (-len(list(set(x))), x))))