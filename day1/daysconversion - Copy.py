# converting days into years and months 

# with arguments and without return type

def dayconversion(day):
    y=day//365
    m=day//30
    print(f'year={y} and months = {m}')


day=int(input("Enter no.of days"))
print(dayconversion(day))