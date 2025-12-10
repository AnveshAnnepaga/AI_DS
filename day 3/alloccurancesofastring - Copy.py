# def occ(s):
#     count = 0
#     for i in s:
#         if c == char:
#             count += 1
#     return count

# s = input("Enter a string: ")
# c = input("Enter a character to count: ")
# print(occ(s, c))



def allocc(s):
    counts = {}
    for i in s:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    max_count = max(counts.values())
    min_count = min(counts.values())
    return min_count, max_count, counts

s = input("Enter a string: ")
min_occ, max_occ, counts = allocc(s)
print(f"Minimum occurrence: {min_occ}")
print(f"Maximum occurrence: {max_occ}")
print(f"All counts: {counts}")

