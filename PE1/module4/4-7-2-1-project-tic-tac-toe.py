from random import randrange

# Define constant values 
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
    for row in range(3):
        print(LINE)
        print(EMPTY_LINE)
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print(EMPTY_LINE)
    print(LINE)

# Call the function to display initial board
display_board(board)

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
            col = (move-1) % 3
            # Check if position is already taken
            if board[row][col] in ['O','X']:
                print("That position is already taken!")
                continue
            # Make the move
            board[row][col] = 'O'
            display_board(board)
            return
        except ValueError:
            print("That's not a valid number!")

enter_move(board)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass
