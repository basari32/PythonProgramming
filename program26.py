string=input("enter string:")
if string[-3:]=='ing':
    string+='ly'
else:
    string+='ing'
print(string)