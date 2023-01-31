while True:
    n = input("Введите римское число: ").upper()
    ar_num = 0
    if n != "0":
        for i in range(len(n)):
            if n[i] == "M":
                if i > 0 and n[i - 1] == "C":
                    ar_num += 0
                else:
                    ar_num += 1000
            elif n[i] == "D":
                if i > 0 and n[i - 1] == "C":
                    ar_num += 0
                else:
                    ar_num += 500
            elif n[i] == "C":
                if i > 0 and n[i - 1] == "X":
                    ar_num += 0
                elif i < (len(n)-1) and n[i+1] == "M":
                    ar_num += 900
                    i += 1
                elif i < (len(n)-1) and n[i+1] == "D":
                    ar_num += 400
                    i += 1
                else:
                    ar_num += 100
            elif n[i] == "L":
                if i > 0 and n[i - 1] == "X":
                    ar_num += 0
                else:
                    ar_num += 50
            elif n[i] == "X":
                if i > 0 and n[i - 1] == "I":
                    ar_num += 0
                elif i < (len(n)-1) and n[i+1] == "C":
                    ar_num += 90
                    i += 1
                elif i < (len(n)) and n[i+1] == "L":
                    ar_num += 40
                    i += 1
                else:
                    ar_num += 10
            elif n[i] == "V":
                if i > 0 and n[i - 1] == "I":
                    ar_num += 0
                else:
                    ar_num += 5
            elif n[i] == "I":
                if i < (len(n) - 1) and n[i+1] == "X":
                    ar_num += 9
                    i += 1
                elif i < (len(n) - 1) and n[i+1] == "V":
                    ar_num += 4
                    i += 1
                else:
                    ar_num += 1
        print(f'Римское число: {n} - арабское число: {ar_num}')
    else:
        print(f'Римское число: {n} - арабское число: {ar_num}')
        break