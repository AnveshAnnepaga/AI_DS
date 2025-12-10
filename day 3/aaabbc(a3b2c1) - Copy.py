def occ(s):
    if not s:
        return ""
    
    res =""
    c=1
    prev=s[0]
    for i in s[1:]:
        if i == prev:
            c+=1
        else:
            res +=prev+str(c)
            prev=i
            c=1
    res+=prev+str(c)
    return res

s=input()
print(occ(s))