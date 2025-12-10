a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
def biggest(x,y,z):
    if x>y and x>z:
        return "a is big"
    elif y>x and y>z:
        return "b is big"
    else:
        return "c is big"
    
print(biggest(a,b,c))