# def evenorodd(num):
#     if num%2 == 0:
#         print("even")
#     else:
#         print("odd")
        
# num=int(input("Enter the numbers:"))
# evenorodd(num)


# def pos_neg(x):
#     return "pos" if x>0 else "neg"


# num=int(input("Enter number:"))
# print(pos_neg(num))


# def div(x):
#     if x%5==0 and x%11 == 0:
#         print("yes") 
#     else:
#         print("no")
        
# x=int(input("Enter number"))
# div(x)


# def year(x):
#     if x%400 == 0 or (x%100 !=0 and x%4==0):
#         return "leap"
#     else:
#         return "not a leap"
    
# x=int(input("enter year:"))
# print(year(x))    


# def alpha(x):
#     return "alpha" if x.isalpha() else "not a alpha"
# x=input("Enter:")
# print(alpha(x))


def vowels(x):
    vow={'a','e','i','o','u','A','E','I','O','U'}
    if x in vow:
        return "vowels"
    else:
        return "consonant"
    
x=input("enter:") 
print(vowels(x))   