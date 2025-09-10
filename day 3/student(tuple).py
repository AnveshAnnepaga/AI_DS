def student():
    students = []
    for i in range(2):
        rollno = int(input("Roll No: "))
        name = input("Name: ")
        marks = list(map(int, input("Enter marks for 3 subjects  ").split()))

        
        students.append([rollno, name, marks])
    tu=tuple(students)
    for i in tu:
        print(i)

    print()    
    max= -1
    topper_name=""
    for student in students:
        for i in student[2]: 
            if i > max:
                max = i
                topper_name=students[1]
    print(f'{topper_name} got highest mark and marks are {max}')

student()
