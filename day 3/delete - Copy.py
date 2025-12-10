list1=[2,1,3,4,5]
list=[]
k=int(input())
for i in range(len(list1)):
    if i==k:
        continue
    else:
        list.append(list1[i])
    
print(list)