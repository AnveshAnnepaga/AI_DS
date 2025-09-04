def func(x):
    for i in  range(1,x):
        temp=i
        rev=0
        while temp>0:
            dig = temp%10
            rev=rev*10+dig
            temp=temp//10
            
            if i==rev:
                print(i,end=" ")




x=int(input("Enter the range: "))
func(x)
            