def freq(lst):
    freq = [0]*10
    for i in lst:
        if i == 0:
            freq[0] += 1
        else:
            n = i
            while n > 0:
                dig = n % 10
                freq[dig] += 1
                n = n // 10
    return freq

lst = [12, 12, 34, 56, 7, 8, 8, 8]
fr = freq(lst)

for i in range(10):
    print(f'{i} -> {fr[i]}')
