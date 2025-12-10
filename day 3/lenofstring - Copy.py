def string(str,s):
    c=0
    for i in str:
        c+=1
    print(c)

    string = str+s
    print(string)
    print(str ==s)

str=input()
s=input()
string(str,s)