name=str(input("Enter student name:"))
number=int(input("Enter student number:"))
maths=int(input("Enter the marks in maths:"))
physics=int(input("Enter the marks in physics:"))
chemistry=int(input("Enter the marks in chemistry:"))

total_marks=maths+physics+chemistry
average=round(total_marks/3,2)
print(f'name is {name} , number is {number} ,total marks is {total_marks} and average is {average}')
