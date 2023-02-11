n = int(input("Введите арабское число: "))
arab_rom = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
            (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def arabic_to_roman(n):
    rom_num = []
    while n > 0:
        for i, r in arab_rom:
            while n >= i:
                rom_num.append(r)
                n -= i
    return ''.join(map(str, rom_num))
print(f"Арабское число {n} - это римское число {arabic_to_roman(n)}")