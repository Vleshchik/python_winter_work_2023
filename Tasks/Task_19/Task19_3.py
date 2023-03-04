class Person:
    def __init__(self, surname, name, second_name):
        self.surname = surname
        self.name = name
        self.second_name = second_name
    def __str__(self):
        return f'{self.second_name[::-1]}{self.name[::-1]}{self.surname[::-1]}'

p = Person(input('Введите фамилию: '), input('Введите имя: '),input('Введите отчество: '))
print(p)