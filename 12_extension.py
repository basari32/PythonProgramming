# Prompt the user for a file name
name = input("Enter the file name: ")

# Extract and print the extension
if '.' in name:
    extension = name.split('.')
    print(extension[-1])
    # print(f"The extension of the file is: {extension}")
else:
    print("The file has no extension.")
