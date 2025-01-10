names=["muhammed","fasil","amal","arun"]
count=0
for x in names:
    for i in x:
        if i  == 'a':
            count+=1
print("Number of 'a' in given list is",count)