# list1=["red", "blue", "green", "yellow", "purple"]
# list2=["blue", "yellow", "black"]
# result=set(list1)-set(list2)
# print(result)
list1=input("Enter color for list1 separate by comma:")
list2=input("Enter color for list2 separate by comma:")
l1=list1.split(',')
l2=list2.split(',')
result=set(l1)-set(l2)
print(result)
