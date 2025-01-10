length=int(input("Enter the limit: "))
num=[]
remove_even=[]
for x in range(length):
    a=int(input("Enter number : "))
    num.append(a)
for x in num:
    if x % 2 != 0:
        remove_even.append(x)
print(remove_even)