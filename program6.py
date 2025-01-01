l1=[]
l2=[]
n=int(input("enter a limit:"))
for i in range(n):
    u=int(input("enter values:"))
    l1.append(u)
print(l1)
m=int(input("enter a limit:"))
for i in range(m):
        v=int(input("enter values:"))
        l2.append(v)
print(l2)
if len(l1) == len(l2):
print("length are  same")
else:
print("length are not same")

if sum(l1) == sum(l2):
    print("sum of l1=l2")
else:
    print("sum of l1!=l2")
    flag = 0
    for x in l2:
        if x in l1:
            flag = 1
            if flag == 1:
                print("there is  common element")
            else:
                print("there is no common element")