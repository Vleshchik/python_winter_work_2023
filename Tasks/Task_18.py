class Lesson:
    def __init__(self, *lessons):
        self.lessons = list(lessons)
    def __getitem__(self, i):
        return self.lessons[i]
class Teacher:
    def __init__(self):
        self.work = 0
    def teach(self, lessons, *pupil):
        for i in pupil:
            i.take(lessons)
            self.work += 1
    def set_task(self):
        for i in lessons:
            i.take(lessons)

class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
class Task:



lesson = Lesson('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marIvanna = Teacher()
vasya = Pupil()
petya = Pupil()
