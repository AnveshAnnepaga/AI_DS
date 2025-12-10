list1 = []
n=int(input())
def func(list1,n):
    for i in range(n):
        list1.append(int(input()))
    
    for i in list1:
        if i<0:
            print(i)


print(func(list1,n))