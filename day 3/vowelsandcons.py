def vowels(s):
    vowelst = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vow = 0
    con = 0
    for i in s:
        if i in vowelst:
            vow += 1
        else:
            con += 1
    return vow, con  

x = input("Enter a string: ")
v, c = vowels(x)
print(f"Number of vowels: {v}")
print(f"Number of consonants: {c}")
