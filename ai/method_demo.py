class student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def show(self):
        print("student name:",self.name)
        print("CGPA:",self.cgpa)
student1=student("paryag",8.5)
student1.show()