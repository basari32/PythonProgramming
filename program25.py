def char_counts(str):
    counts=dict()
    words=str.strip()
    for char in words:
        if char in counts:
            counts[char]+=1
        else:
            counts[char]=1
    return counts
str=input("enter the string:")
print(char_counts(str))
