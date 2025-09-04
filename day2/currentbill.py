def currentbill(units):
    if units<=50:
        return 50*3.80
    elif units>=51 and units <100:
        return (50*3.80)+((units-50)*4.2)
    elif units>=100 and units<200:
        return (50*3.80)+((units-50)*4.20)+((units-100)*5.10)
    elif units>=200 and units<=300:
        return (50*3.80)+((units-50)*4.20)+((units-100)*5.10)+((units-200)*6.30)
    else:
        return (50*3.80)+((units-50)*4.20)+((units-100)*5.10)+((units-200)*6.30)+((units-300)*7.50)
    

# cn,pmr,lmr=map(int,input("Enter:").split())
# cname = input("enter name:")
units =int(input("enter:"))   
print(currentbill(units))    