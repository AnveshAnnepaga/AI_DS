def secondmax(lst):
    for i in range(6):
        lst.append(int(input()))
    
    max = lst[0]
    for i in lst:
        if i > max:
            max_val = i

    secondmax = None
    for i in lst:
        if i < max_val:
            if secondmax is None or i > secondmax:
                secondmax = i

    return secondmax

list = []
print("second max ",secondmax(list))
