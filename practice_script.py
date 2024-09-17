
def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_list(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[i][col] for i in range(9)]
        if not is_valid_list(column):
            return False
    
    # Check 3x3 subgrids
    for i in range(3):
        for j in range(3):
            subgrid = [board[row][col] for row in range(3*i, 3*i+3) for col in range(3*j, 3*j+3)]
            if not is_valid_list(subgrid):
                return False
    
    return True

def is_valid_list(lst):
    seen = set()
    for num in lst:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True

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
