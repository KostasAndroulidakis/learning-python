# Asks user to enter the number of blocks
blocks = int(input("Enter the number of blocks: "))

# Create a variable for the height
height = 0

# Create a variable for the block per layer
layer_blocks = 1    # first layer

# Create a variable for the remaining blocks
remaining_blocks = blocks

# while loop
while remaining_blocks >= layer_blocks:
    remaining_blocks -= layer_blocks    # subtract used blocks
    height += 1    # add 1 for each layer
    layer_blocks += 1    # one block for the next layer
    
# Prints the final height
print("The height of the pyramid:", height)
