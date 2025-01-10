# Input strings
string1 = input("Enter a word:")
string2 = input("Enter a word:")

# Swap the second character
s1 = string1[0] + string2[1] + string1[2:]
s2 = string2[0] + string1[1] + string2[2:]

# Combine into a single string
result = s1 + " " + s2

# Print the result
print(result)
