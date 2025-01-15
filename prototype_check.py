
def check_subgrid(board, start_row, start_col):
    nums = set()
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] in nums:
                return False
            nums.add(board[i][j])
    return True

def check_row(board, row):
    nums = set()
    for col in range(9):
        if board[row][col] in nums:
            return False
        nums.add(board[row][col])
    return True

def check_col(board, col):
    nums = set()
    for row in range(9):
        if board[row][col] in nums:
            return False
        nums.add(board[row][col])
    return True

def is_valid_sudoku(board):
    for i in range(9):
        if not check_row(board, i) or not check_col(board, i):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
           if not check_subgrid(board, i, j):
               return False

    return True

# Example Sudoku solution
sudoku_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

if is_valid_sudoku(sudoku_board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
