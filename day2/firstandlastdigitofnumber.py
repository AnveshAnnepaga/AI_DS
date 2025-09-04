# finding first and last digit of a number
def fun(num):
    first=num
    while first>=10:
        first=first//10
    last=num%10
    return first,last

print(fun(1234))

# another way
# def fun(num):
    s=str(num)
    return int(s[0]),int(s[-1])
    
print(fun(1234))

# sum of last and first digit

def sum(num):
    first=num
    while first>=10:
        first=first//10
    last=num%10
    return first+last
print(sum(1234))