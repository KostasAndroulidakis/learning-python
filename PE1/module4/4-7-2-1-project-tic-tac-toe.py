from random import randrange

# Constants
LINE = "+-------+-------+-------+"
EMPTY_LINE = "|       |       |       |"
COMPUTER = "X"
USER = "O"

# Define initial board
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# First move by computer - always in the middle
board[1][1] = "X"

def display_board(board):
    # Display 3x3 game board with grid lines
    for row in range(3):
        print(LINE)
        print(EMPTY_LINE)
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print(EMPTY_LINE)
    print(LINE)

def enter_move(board):
    while True:
        try:
            # Get user input and convert to integer
            move = int(input("Enter your move: "))
            # Validate number is in range 1-9
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9")
                continue
            # Calculate row and column from move
            row = (move-1) // 3  
            column = (move-1) % 3
            # Check if position is already taken
            if board[row][column] in ['O','X']:
                print("That position is already taken!")
                continue
            # Make the move
            board[row][column] = 'O'
            display_board(board)
            return
        except ValueError:
            print("That's not a valid number!")

def make_list_of_free_fields(board):
    # Return list of (row, col) tuples for empty squares
    free_fields = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['O', 'X']:
                free_fields.append((row, column))
    return free_fields

# Check for victory
def victory_for(board, sign):
    # Check rows
    for row in range(3):
        if all(board[row][column] == sign for column in range(3)):
            return True
    # Check columns
    for column in range(3):
        if all(board[row][column] == sign for row in range(3)):
            return True
    # Check diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

def draw_move(board):
    # check available free fields
    free_fields = make_list_of_free_fields(board)
    # choose a random number
    random_number = randrange(len(free_fields))
    random_tuple = free_fields[random_number]
    row, column = random_tuple
    # computer's move
    board[row][column] = "X"

# game main loop
while True:   # continue until return or break
    display_board(board)
    # User move
    enter_move(board)
    if victory_for(board, USER):
        print("You won!")
        break
    # Computer move
    draw_move(board)
    if victory_for(board, COMPUTER):
        display_board(board)
        print("Computer won!")
        break
    # check for tie
    elif not make_list_of_free_fields(board):
        print("Tie!")
        break
