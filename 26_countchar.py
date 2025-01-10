def char_count(str):
    counts=dict()
    words=str.strip()
    for char in words:
        if char in counts:
            counts[char]+=1
        else:
            counts[char]=1
    return counts
str=input("Enter the string:")
print(char_count(str))
