class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
    
    def display(self):
        print(f'name of emp is {self.name} and salary is {self.salary}')


class Manager(Employee):
    def __init__(self, name, salary,dept):
        super().__init__(name, salary)
        self.dept=dept

    def display(self):
        print(f'name is {self.name} , salary is {self.salary} and dept is {self.dept}')


e1=Employee("Anvesh",500000)
e1.display()
m = Manager("Bharath",4000,"Data Science")
m.display()