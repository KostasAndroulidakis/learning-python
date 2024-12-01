# The existing list of numbers hidden in the hat.
hat_list = [1, 2, 3, 4, 5]

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Enter an integer number: "))

# Step 2: write a line of code that removes the last element from the list.
hat_list.pop()  # Permanently removes the last element.

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)