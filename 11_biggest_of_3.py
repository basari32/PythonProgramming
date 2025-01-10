a=int(input("Enter first number :" ))
b=int(input("Enter second number :" ))
c=int(input("Enter third number :" ))
if a > b and b > c:
    print("Biggest number is",a)
elif b > c:
    print("Biggest number is",b)
else:
    print("Biggest number is",c)
