class Dog:
    def __init__(self, name, age, breed, sex):
        self.name = name
        self.age = age
        self.breed = breed
        self.sex = sex

    def get_info(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age) + ' years')
        print('breed: ' + self.breed)
        print('sex: ' + self.sex)

    def add_one(self, x):
        return x+1

    def bark(self):
        print('bark')

    def set_age(self, age):
        self.age = age


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        total_grade = 0
        for student in self.students:
            total_grade += student.grade

        return total_grade/len(self.students)


s1 = Student('Vardaan', 15, 95)
s2 = Student('Aryan', 11, 100)
s3 = Student('Tim', 17, 90)

course = Course('Science', 2)

course.add_student(s1)
course.add_student(s2)

print(course.get_average_grade())