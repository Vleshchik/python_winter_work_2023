s = list(str(input()))#АГЦТАЦГТАТГЦГАТАЦАТТГТААТЦТГЦАГТГЦТАЦАТЦГГАТЦГААТЦГАТАЦГТТАЦТЦТГААГТГЦТГТАГТГТАГЦГАТ
def dna(s):
    for i in range(len(s) - 1):
        if s[i] == "А" and s[i + 1] == "Г":
            s[i] = "Г"
            s[i + 1] = "А"
        elif s[i] == "Г" and s[i + 1]  == "А":
            s[i] = "А"
            s[i + 1] = "Г"
        elif s[i] == "Ц" and s[i + 1]  == "Т":
            s[i + 1] = "АГТ"
            i += 3
        elif s[i] == "Т" and s[i + 1] == "Ц":
            s[i + 1] = "АГЦ"
            i += 3
    s = ''.join(s)
    return s
print(dna(s))