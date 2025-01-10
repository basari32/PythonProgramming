def length(words):
    return max(len(word) for word in words)

words_list = input("Enter a list of words separated by spaces: ").split()
print("Length of the longest word:", length(words_list))
