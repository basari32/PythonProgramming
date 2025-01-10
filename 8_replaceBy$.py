def replace_char(str):
    char=str[0]
    str=str.replace(char,'$')
    str=char+str[1:]
    return str
str=input("Enter the word:")
print(replace_char(str))
