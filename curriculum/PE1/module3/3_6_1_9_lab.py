# the list we have
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# the list we need
new_list = []

for element in my_list:
    if element not in new_list:
        new_list.append(element)

print("The list with unique elements only:")
print(new_list)