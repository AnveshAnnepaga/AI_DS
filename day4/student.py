class Student:
    def __init__(self,name,rollno,marks):
        self._name = name
        self.rollno=rollno
        self.marks=marks
    
    def display(self):
        print("name of student is:",self._name)
        print("roll no of student is:",self.rollno)
        print("marks of student is:",self.marks)

stu = Student("Anvesh","67D2",[20,30,50])
stu.display()

stu2=Student("Bharath","67D6",[30,50,70])
stu2.display()

class Teacher(Student):
    def __init__(self, name, rollno, marks):
        super().__init__(name, rollno, marks)


t=Teacher("Anvesh",56616,256)
print(t.name)