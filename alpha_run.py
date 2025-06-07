
def is_valid_sudoku(board):
    def is_valid_row(board):
        for row in board:
            if not is_valid_set(row):
                return False
        return True

    def is_valid_column(board):
        for col in range(9):
            if not is_valid_set([row[col] for row in board]):
                return False
        return True

    def is_valid_subgrid(board, start_row, start_col):
        subgrid = [board[i][j] for i in range(start_row, start_row+3) for j in range(start_col, start_col+3)]
        return is_valid_set(subgrid)

    def is_valid_set(nums):
        seen = set()
        for num in nums:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    for i in range(9):
        if not is_valid_row(board[i]):
            return False
    for j in range(9):
        if not is_valid_column(board):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_subgrid(board, i, j):
                return False

    return True

# Sudoku board for testing
sudoku_board = [
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

if is_valid_sudoku(sudoku_board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
