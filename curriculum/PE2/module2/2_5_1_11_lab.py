# Define constant
SUDOKU = [[2,9,5,7,4,3,8,6,1],
          [4,3,1,8,6,5,9,2,7],
          [8,7,6,1,9,2,5,4,3],
          [3,8,7,4,5,9,2,1,6],
          [6,1,2,3,8,7,4,9,5],
          [5,4,9,2,1,6,7,3,8],
          [7,6,3,5,2,4,1,8,9],
          [9,2,8,6,7,1,3,5,4],
          [1,5,4,9,3,8,6,7,2]]

# Prepare an empty list for user input
user_input = []

# Ask user for input
sample_input = input("Enter sudoku: ")

# Split string into list of strings
rows = sample_input.split() 

# Convert each string to list of integers
for row in rows:
    user_input.append([int(digit) for digit in row])
    