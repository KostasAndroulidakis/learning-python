# 2.5.1.11 LAB: Sudoku

# Validate 9x9 Sudoku grid

user_input = []
sample_input = input("Enter sudoku: ")
rows = sample_input.split() 

# Convert each string to list of integers
for row in rows:
    user_input.append([int(digit) for digit in row])

# Valid Sudoku digits
CORRECT_DIGITS = set(range(1, 10))

# Verify each row contains all digits 1-9
def check_rows(grid):
    for row in grid:
        if set(row) != CORRECT_DIGITS:
            return False
    return True

# Verify each column contains all digits 1-9
def check_columns(grid):
    for row in zip(*grid):
        if set(row) != CORRECT_DIGITS:
            return False
    return True

# Verify each 3x3 subsquare contains all digits 1-9
def check_subsquares(grid):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subsquare = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    subsquare.add(grid[i][j])
            if subsquare != CORRECT_DIGITS:
                return False
    return True

# Validate Sudoku grid against all rules
def triple_check(grid):
    return check_rows(grid) and check_columns(grid) and check_subsquares(grid)

print("Yes" if triple_check(user_input) else "No")
