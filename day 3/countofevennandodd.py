list=[2,3,4,5,8,10]
def evenodd(list):
    even =0
    odd =0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

print(evenodd(list))