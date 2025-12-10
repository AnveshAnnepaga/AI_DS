x=int(input("Enter a number:"))
def fun(n):
    d={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
    s=""
    while n>0:
        r=n%10
        s=d[r]+" "+s
        n=n//10
    return s    
print(fun(x))