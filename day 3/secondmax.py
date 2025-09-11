# def secondmax(lst):
#     for i in range(6):
#         lst.append(int(input()))
    
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i

#     secondmax = None
#     for i in lst:
#         if i < max:
#             if secondmax is None or i > secondmax:
#                 secondmax = i

#     return secondmax

# list = []
# print("second max ",secondmax(list))



def secondmax(l):
    if len(l) < 2:
        return None  
    
    max1 = max(l[0], l[1])
    max2 = min(l[0], l[1])
    
    for i in l[2:]:
        if i > max1:
            max2 = max1
            max1 = i
        elif max2 < i < max1:
            max2 = i
    
    return max2

l = [10, 5, 8, 12, 7]
print(secondmax(l))  
