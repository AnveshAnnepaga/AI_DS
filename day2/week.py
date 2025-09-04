def week(x):
    if x==0:
        return "sunday"
    elif x==1:
        return "monday"
    elif x==2:
        return "Tuesday"
    elif x==3:
        return "wednesday"
    elif x==4:
        return "Thursday"
    elif x==5:
        return "Friday"
    elif x==6:
        return "Saturday"
    else:
        return "Invalid number"
    
x=int(input("Enter:"))
print(week(x))