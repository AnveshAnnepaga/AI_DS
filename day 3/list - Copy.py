list1 = []
n=int(input())
def func(list1,n):
    for i in range(n):
        list1.append(int(input()))
    
    return list1


print(func(list1,n))