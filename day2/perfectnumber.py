def func(x):
    for i in range(2,x):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum=sum+j
        
        if sum==i:
            print(i,end=" ")    
                


x=int(input("Enter the range: "))
func(x)