import statistics

students = []
lectors = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)


    def statistic_average(self):
        self.average = statistics.mean([j for i in self.grades.values() for j in i])
        return self.average


    def lector_grade(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades_lector:
                lector.grades_lector[course] += [grade]
            else:
                lector.grades_lector[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name = f'Имя: {self.name}'
        family = f'Фамилия: {self.surname}'
        average = f'Средняя оценка за домашние задания: {self.statistic_average()}'
        c = ', '.join(self.courses_in_progress)
        course = f'Курсы в процессе изучения: {c}'
        f = ', '.join(self.finished_courses)
        finish = f'Завершенные курсы: {f}'
        some_student = f'{name}\n{family}\n{average}\n{course}\n{finish}'
        print(some_student)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет данных')
            return
        return self.statistic_average() > other.statistic_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lector = {}
        lectors.append(self)

    def statistic_average(self):
        self.average = statistics.mean([j for i in self.grades_lector.values() for j in i])
        return self.average

    def __str__(self):
        name = f'Имя: {self.name}'
        family = f'Фамилия: {self.surname}'
        average = f'Средняя оценка за лекции: {self.statistic_average()}'
        some_lecturer = f'{name}\n{family}\n{average}'
        print(some_lecturer)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Eror")
            return
        return self.statistic_average() < other.statistic_average()


class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res1 = f'Имя: {self.name}'
        res2 = f'Фамилия: {self.surname}'
        some_reviewer = f'{res1}\n{res2}'
        print(some_reviewer)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def statistic_student(students=students, course='Python'):
    res = []
    for student in students:
        if course in student.grades.keys():
            for values in student.grades.values():
                res += values
            return f'Средний бал студентов по лекции {course}: {statistics.mean(res)}'


def statistic_lector(lectors=lectors, course='Python'):
    res = []
    for lector in lectors:
        if course in lector.grades_lector.keys():
            for values in lector.grades_lector.values():
                res += values
            return f'Средний бал лекторов по лекции {course}: {statistics.mean(res)}'


student1 = Student('Morty', 'Smith', 'm')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Rick', 'Sunchez', 'm')
student2.courses_in_progress += ['Java', 'Django']
student2.finished_courses += ['Межпланетное путешествие']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Sam', 'Body')
reviewer2.courses_attached += ['Java']

reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer2.rate_hw(student2, 'Java', 8)
reviewer2.rate_hw(student2, 'Java', 7)
reviewer2.rate_hw(student2, 'Java', 10)

lector1 = Lecturer('Kety', 'New')
lector1.courses_attached += ['Python']

lector2 = Lecturer('Mill', 'Pops')
lector2.courses_attached += ['Java']

student1.lector_grade(lector1, 'Python', 9)
student1.lector_grade(lector1, 'Python', 1)
student1.lector_grade(lector1, 'Python', 10)

student2.lector_grade(lector2, 'Java', 5)
student2.lector_grade(lector2, 'Java', 7)
student2.lector_grade(lector2, 'Java', 4)

#rate_hw
print(student1.grades)
print(student2.grades)
print()

#lector_grade
print(lector1.grades_lector)
print(lector2.grades_lector)
print()

#__str__
reviewer1.__str__()
print()
lector1.__str__()
print()
student1.__str__()
print()

reviewer2.__str__()
print()
lector2.__str__()
print()
student2.__str__()
print()

#средний бал
print(lector2.statistic_average())
print()
print(lector1.statistic_average())
print()
print(student2.statistic_average())
print()
print(student1.statistic_average())
print()

#сравнение
print(lector2.__lt__(lector1))
print(student1.__lt__(student2))

#4.1
print()
print(statistic_student(students, 'Python'))
print(statistic_student(students, 'Java'))

#4.2
print()
print(statistic_lector(lectors, 'Python'))
print(statistic_lector(lectors, 'Java'))

