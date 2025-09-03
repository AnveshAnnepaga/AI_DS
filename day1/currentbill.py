cn,pmr,lmr=map(int,input("Enter:").split())
cname = input("enter name:")
units =pmr-lmr
currentbill=round(units*3.80,2)
print(f'units are {units}')
print(f'name={cname}\nconsumer number ={cn}\npresent month bill ={pmr}\nlast month bill = {lmr}\ncurrent bill = {currentbill}')
