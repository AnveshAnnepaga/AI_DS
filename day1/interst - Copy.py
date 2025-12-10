principle_am = int(input("enetr principle amount"))
rate = int(input("enter rate of interst"))
time = int(input("enter no.of months"))

interst = principle_am*rate*time/100
print(interst)

total = principle_am+interst
print(total)