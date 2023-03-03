sen_1 = tuple(input().split(', ')) #мастер и маргарита, пятнадцатилетний капитан, война и мир, вокруг света за 80 дней
sen_2 = tuple(input().split(', ')) #война и мир, не время для драконов, мир без радости, ночной дозор, мастер и маргарита
pupil_1 = set(sen_1)
pupil_2 = set(sen_2)
uni_books = pupil_1.intersection(pupil_2)
print(str(len(uni_books)))