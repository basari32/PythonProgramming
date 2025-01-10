list1 = []
list2 = []
sum1=0
sum2=0
f=0
limit1 = int(input("Enter the limit of first list:"))
for x in range(limit1):
    val = int(input("Enter value:"))
    list1.append(val)
limit2 = int(input("Enter the limit of second list:"))
for x in range(limit2):
    val = int(input("Enter value:"))
    list2.append(val)
if len(list1) == len(list2):
    print("Given list is same length")
else:
    print("Given list is not same length")
for x in list1:
    sum1+=x
for x in list2:
    sum2+=x
if sum1==sum2:
    print("Sum is same")
else:
    print("Sum is not same")
for x in list1:
    for y in list2:
        if x==y:
            f=1
            break
if f==1:
    print("a value occure in both list")
else:
    print("value not occure in both list")
