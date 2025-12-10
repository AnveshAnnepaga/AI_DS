def count_duplicates(lst):
    unique = []
    duplicates = 0
    for i in lst:
        if i in unique:
            duplicates += 1 
        else:
            unique.append(i) 
    return duplicates

lst = [12, 12, 34, 56, 7, 8, 8, 8]
dup_count = count_duplicates(lst)
print("Number of duplicate elements:", dup_count)
