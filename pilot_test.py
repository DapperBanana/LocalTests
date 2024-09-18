
def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_group(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[i][col] for i in range(9)]
        if not is_valid_group(column):
            return False
    
    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[i+x][j+y] for x in range(3) for y in range(3)]
            if not is_valid_group(subgrid):
                return False
            
    return True

def is_valid_group(group):
    group = [num for num in group if num != "."]
    return len(group) == len(set(group))

# Example Sudoku board
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

if is_valid_sudoku(board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
