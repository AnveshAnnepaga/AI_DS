def fib(x):
    fib1=0
    fib2=1
    for i in range(x):
        print(fib1,end=" ")
        fib3=fib1+fib2
        fib1=fib2
        fib2=fib3
    

x=int(input("Enter the range: "))
fib(x)