l=[1,-6,5,7,6,-9,-1]
c=[x for x in l if x>=0]
print(c)

l=[2,3,4,5]
c=[x * x for x in l]
print(c)

l=input("enter a word:")
c=[x for x in l if x in "a,e,i,o,u"]
print(c)

word=input("enter a word:")
ordinalvalues=[ord(char)for char in word]
print("ordinalvalues of each character in", word,":",ordinalvalues)