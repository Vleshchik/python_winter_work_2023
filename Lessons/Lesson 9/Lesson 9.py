fi = open("Test.txt", "r", encoding="UTF-8")
fo = open("test1.txt", "w", encoding="UTF-8")
lst = fi.readlines()
for i in lst:
    fo.write(i[::2])


