
old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56}

new_dict = dict([(value, key) for key, value in old_dict.items()])


print ("Dictionary after swapping is : ")
print(new_dict)

