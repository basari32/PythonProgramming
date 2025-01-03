l=[]
n=int(input("enter a limit:"))
for i in range (n):
    v=int(input("enter values:"))
    l.append(v)
print(l)
sum=0
for x in l:
    sum=sum+x
print("sum of all items=",sum)
