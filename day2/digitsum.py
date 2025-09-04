def digit(num):
    sum =0
    while num>0:
        dig=num%10
        sum=sum+dig
        num=num//10
    return sum
n=int(input("Enter n:"))
print(digit(n))