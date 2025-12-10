def unique(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

lst = [12, 12, 34, 56, 7, 8, 8, 8]
unq = unique(lst)
print("Unique elements:", unq)
