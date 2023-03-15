import keyword
s = input().split() #False None Nonet True false and Andy as assert async await break class continue def defence del delay elif else except finally for forward from global apple if import in is island lambda nonlocal not or pass password raise return try while with yield
for i in range(len(s)):
    if keyword.iskeyword(s[i]):
        s[i] = '<kw>'

print(' '.join(s))


