
def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_list(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_list(column):
            return False
    
    # Check 3x3 grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_list(grid):
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

# Example Sudoku solution
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
    print("This is a valid Sudoku solution.")
else:
    print("This is not a valid Sudoku solution.")
