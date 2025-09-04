# strong number = sum of factorial of digits is equal to the number itself
# e.g 145 = 1! + 4! + 5! = 145

# from math import factorial  (predefined function)
def func(x):
    for i in range(1,x):
        temp=i
        sum=0
        while temp>0:
            dig = temp%10
            def fact(dig):
                if dig == 0 or dig == 1:
                    return 1
                else:
                    return dig * fact(dig - 1)
            
            sum=sum+fact(dig)
            temp=temp//10
        if i==sum:
            print(i,end=" ")
            

x=int(input("Enter the range: "))
func(x)
                      