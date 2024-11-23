
board = [
    ["1", "2", "3"],  
    ["4", "5", "6"],  
    ["7", "8", "9"]   
]

line = "+-------+-------+-------+"
empty_line = "|       |       |       |"
number_line = f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |"

def display_board(board):
    for row in range(3):
        print(line)
        print(empty_line)
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print(empty_line)
    print(line)
