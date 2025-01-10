my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
asc_dict = dict(sorted(my_dict.items()))
des_dict = dict(sorted(my_dict.items(), reverse=True))
print("Original Dictionary:", my_dict)
print("Ascending Order:", asc_dict)
print("Descending Order:", des_dict)
