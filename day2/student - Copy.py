def student(maths, physics, chemistry):
    if maths > 40 and physics > 40 and chemistry > 40:
        if maths < 50 and physics < 50 and chemistry < 50:
            return "Grade C"
        elif maths <= 70 and physics <= 70 and chemistry <= 70:
            return "Grade B"
        elif maths <= 80 and physics <= 80 and chemistry <= 80:
            return "Grade A"
        else:
            return "Distension"
    else:
        return "student is fail"


maths = int(input("Enter the marks in maths:"))
physics = int(input("Enter the marks in physics:"))
chemistry = int(input("Enter the marks in chemistry:"))
print(student(maths,physics,chemistry))