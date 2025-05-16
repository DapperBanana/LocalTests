
def is_valid_sudoku(board):
    # Check rows
    for i in range(9):
        row_set = set()
        for j in range(9):
            if board[i][j] in row_set:
                return False
            if board[i][j] != ".":
                row_set.add(board[i][j])

    # Check columns
    for j in range(9):
        col_set = set()
        for i in range(9):
            if board[i][j] in col_set:
                return False
            if board[i][j] != ".":
                col_set.add(board[i][j])

    # Check 3x3 grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grid_set = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if board[row][col] in grid_set:
                        return False
                    if board[row][col] != ".":
                        grid_set.add(board[row][col])

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
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
