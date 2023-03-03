# Класс Урок
class Lesson:
    def __init__(self, *lessons):
        self.lessons = list(lessons)
    def __getitem__(self, i):
        return self.lessons[i]

# Класс Задача
class Task(Lesson):
    def __init__(self):
        self.homework = {}
    def add_task(self):
        t = int(input('Введите количество задач: '))
        for i in range(1, t + 1):
            task = input('Введите название задачи: ')
            self.tasks.append(task)
        self.homework = dict.fromkeys(self.tasks, "not solved")
        return self.homework
    # Метод для проверки задачи ученика
    def check_task(self):
        for k, v in solwed_hv:
            if v == 'solved':
                v = 'confirmed'
            else:
                continue
        return (print(solved_hw))

# Класс Преподаватель
class Teacher(Task):
    def __init__(self, name):
        self.name = name
        self.lessons = []
        self.tasks = []
        self.work = 0
    # Метод для добавления урока
    def teach(self, lessons, *pupil):
        for i in pupil:
            i.take(lessons)
            self.work += 1

# Класс Ученик
class Pupil(Task):
    def __init__(self, name):
        self.name = name
        self.homework = Task.homework
    # Метод для решения задачи
    def solve_task(self, homework):
        for k, v in homework:
            res = input(f'Решена ли {k} (Введите "Yes" или "No"): ')
            if res == 'Yes':
                v = 'solved'
            else:
                continue
        solved_hw = homework
        return print(solved_hw)





MI = Teacher('МарьИванна')
Petya = Pupil('Петя')
MI.add_task()
Petya.solve_task()
MI.check_task()