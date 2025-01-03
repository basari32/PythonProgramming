l=[]
n=int(input("enter a limit:"))
for i in range(n):
    v=int(input("enter values:"))
    l.append(v)
print(l)
c=[x for x in l if x%2!=0]
print("list of non even numbers:",c)
