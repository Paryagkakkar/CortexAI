class Student:

    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa


class Teacher(Student):

    def __init__(self, name, age, cgpa, salary):
        super().__init__(name, age, cgpa)
        self.salary = salary


teacher1 = Teacher("Paryag", 19, 8.7, 10000)

print(teacher1.name)
print(teacher1.age)
print(teacher1.cgpa)
print(teacher1.salary)    