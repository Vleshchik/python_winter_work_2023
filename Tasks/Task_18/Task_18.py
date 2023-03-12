# Класс Урок
class Lesson:
    def __init__(self, *lessons):
        self.lessons = list(lessons)
    def __getitem__(self, i):
        return self.lessons[i]

# Класс Задача
class Task():
    def __init__(self):
        Task.homework = {}
    # Добавление задач
    def add_task(self):
        t = int(input('Введите количество задач: '))
        for i in range(1, t + 1):
            task = input('Введите название задачи: ')
            Teacher.tasks.append(task)
            answer = input('Введите ответ на задачу: ')
            Teacher.answers.append(answer)
        Task.homework = dict.fromkeys(self.tasks, "")
        return Task.homework
    # Метод решения задач учеником
    def solve_task(self):
        self.homework = []
        for k, v in Task.homework.items():
            res = input(f'Введите решение задачи {k}: ')
            self.homework.append(res)
        return self.homework
    # Метод для проверки решения задач учеником
    def check_task(self, *pupil):
        for i in pupil:
            checked_hw = {}
            lst = []
            for j in range(len(Teacher.answers)):
                if Teacher.answers[j] == i.homework[j]:
                    lst.append('confirmed')
                else:
                    lst.append('not solved')
            checked_hw = dict(zip(self.tasks, lst))
            print(f"Результат решения учеником {i.name} домашнего задания: {'; '.join(str(k) + ' - ' + str(v) for k, v in checked_hw.items())}")

# Класс Преподаватель
class Teacher(Task):
    def __init__(self, name):
        self.name = name
        self.lessons = []
        Teacher.tasks = []
        self.work = 0
        Teacher.answers = []
    # Метод для добавления урока
    def teach(self, lessons, *pupil):
        for i in pupil:
            i.take(lessons)
            self.work += 1

# Класс Ученик
class Pupil(Task):
    def __init__(self, name):
        self.name = name
        Pupil.homework = {}

MI = Teacher('МарьИванна')
Petya = Pupil('Петя')
Vasya = Pupil('Вася')
MI.add_task()
Petya.solve_task()
Vasya.solve_task()
MI.check_task(Petya, Vasya)