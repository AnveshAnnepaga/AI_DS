def primeornot(n):
    if n<=1:
        return "not a prime"
    
    if n==2:
        return "is a prime"
    
    for i in range(2,n):
        if n%i==0:
            return "not a prime"
            break
        else:
            return "is a prime"
        
x=int(input("Enter n:"))
print(primeornot(x))