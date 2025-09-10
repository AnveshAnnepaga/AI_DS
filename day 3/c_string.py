def string(str):
    alpha=0
    digit=0
    spec=0
    for i in str:
        if i.isalpha():
            alpha+=1
        elif i.isdigit():
            digit+=1
        else:
            spec+=1
    return alpha,digit,spec

str=input()
print(string(str))