# Prepare an empty list for user input
user_input = []

# Ask user for input
sample_input = input("Enter sudoku: ")

# Split string into list of strings
rows = sample_input.split() 

# Convert each string to list of integers
for row in rows:
    user_input.append([int(digit) for digit in row])

# Check digit in a row
correct_digits = set(range(1, 10))

def check_rows(grid):
    for row in grid:
        if set(row) != correct_digits:
            return False
    return True

def check_columns(grid):
    for row in zip(*grid):
        if set(row) != correct_digits:
            return False
    return True

def check_subsquares(grid):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subsquare = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    subsquare.add(grid[i][j])
            if subsquare != correct_digits:
                return False
    return True

def triple_check(grid):
    return check_rows(grid) and check_columns(grid) and check_subsquares(grid)

print("Yes" if triple_check(user_input) else "No")
