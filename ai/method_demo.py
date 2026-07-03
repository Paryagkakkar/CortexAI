class student:
    def __init__(self,name,age,cgpa):
        self.name=name
        self.age=age
        self.cgpa=cgpa
class teacher(student):
    pass
    def __init__(self,salary):
        super().__init__(name,age)
        self.salary=salary
teacher1=teacher("paryag",19,8.7,10000)
print(teacher1)
        
        