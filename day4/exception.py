a, b = map(int, input().split())

try:
    print("division btwm a andd b", a/b)
except:
    print("not divisible by 0")
else:
    print("error found")
finally:
    print("try by your self(not divisible by 0)")

raise ValueError("b value must be >0")
