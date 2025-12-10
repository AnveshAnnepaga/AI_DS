for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

print()
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("$",end=" ")
        elif i+j==6:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
    
print()

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
    
print()

