def replace_str(str):
   if len(str)<=1:
    return str
   return str[-1]+str[1:-1]+str[0]
str=input("enter a string:")
print(replace_str(str))