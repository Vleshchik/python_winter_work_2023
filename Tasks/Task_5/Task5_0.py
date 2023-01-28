w = input()
l = []
vovels = []
consonants = []
final_w = []
for i in range(len(w)):
    l.append(w[i])
print(l)
for i in range (len(w)):
    if ord(l[i]) == ord('e') or ord(l[i]) == ord('y') or ord(l[i]) == ord('u') or ord(l[i]) \
            == ord('i') or ord(l[i]) == ord('o') or ord(l[i]) == ord('a'):
        vovels.append(l[i])
    else:
        consonants.append(l[i])
if abs(len(vovels) - len(consonants)) >= 2:
    print("Операция невозможна")
else:
    if len(vovels) > len(consonants):
        for i in range(len(consonants)):
            final_w.append(vovels[0])
            vovels.remove(vovels[0])
            final_w.append(consonants[0])
            consonants.remove(consonants[0])
        final_w.append(vovels[0])
        print(final_w)
    elif len(vovels) < len(consonants):
        for i in range(len(vovels)):
            final_w.append(consonants[0])
            consonants.remove(consonants[0])
            final_w.append(vovels[0])
            vovels.remove(vovels[0])
        final_w.append(consonants[0])
        print(final_w)
    else:
        for i in range(len(vovels)):
            final_w.append(consonants[0])
            consonants.remove(consonants[0])
            final_w.append(vovels[0])
            vovels.remove(vovels[0])
        print(final_w)