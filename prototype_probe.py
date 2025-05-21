
def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_row(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [row[col] for row in board]
        if not is_valid_row(column):
            return False

    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_row(subgrid):
                return False

    return True

def is_valid_row(row):
    seen = set()
    for num in row:
        if num != ".":
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
