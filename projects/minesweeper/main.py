"""This is a Minesweeper game implementation in Python."""

def solution(N, R, C):
    # Create an empty board of size N×N
    board = [[0] * N for _ in range(N)]

    # Place bombs at the locations specified by arrays R and C
    for i in range(len(R)):
        row = R[i]
        col = C[i]
        board[row][col] = -1    # Mark locations with -1

    # Calculate the number of neighboring bombs for each non-bomb cell
    for row in range(N):
        for col in range(N):
            # Skip if this cell contains a bomb
            if board[row][col] == -1:
                continue
                
            # Check all 8 neighboring cells
            for dr in [-1, 0, 1]:           # Row offset
                for dc in [-1, 0, 1]:       # Column offset
                    # Skip the current cell itself
                    if dr == 0 and dc == 0:
                        continue
                        
                    # Calculate neighbor coordinates
                    nr = row + dr
                    nc = col + dc
                    
                    # Check if neighbor is within bounds
                    if 0 <= nr < N and 0 <= nc < N:
                        # If neighbor has a bomb, increment the count
                        if board[nr][nc] == -1:
                            board[row][col] += 1

    # Print the final board
    result = []
    for row in board:
        row_str = ""
        for cell in row:
            if cell == -1:
                row_str += "B"  # Bombs are shown as 'B'
            else:
                row_str += str(cell)  # Numbers stay as is
        result.append(row_str)
        
    # Join all rows with newlines and return
    return "\n".join(result)

# Example usage
N=3
R=[2,1,0,2]
C=[0,2,1,2]
print(solution(N, R, C))

N=5
R=[2,3,2,3,1,1,3,1]
C=[3,3,1,1,1,2,2,3] 
print(solution(N, R, C))