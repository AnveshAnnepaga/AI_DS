def validate(x):
    if x.isalpha():
        return "alphabet"
    elif x.isdigit():
        return "digit"
    else:
        return "special character"
   
    
x=input("enter")
print(validate(x))