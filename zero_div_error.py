
try:
    number=100
    x=int(input("enter divisor: "))
    ans=number/x
    print(ans)
except ZeroDivisionError:
    print("Do not divide by 0")