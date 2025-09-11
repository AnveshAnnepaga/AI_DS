class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno=rollno
        self.marks=marks
    
    def display(self):
        print("name of student is:",self.name)
        print("roll no of student is:",self.rollno)
        print("marks of student is:",self.marks)

stu = Student("Anvesh","67D2",[20,30,50])
stu.display()

stu2=Student("Bharath","67D6",[30,50,70])
stu2.display()