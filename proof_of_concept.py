
def is_valid_sudoku(board):
    def check_row(row):
        seen = set()
        for num in row:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    def check_column(col):
        seen = set()
        for num in col:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    def check_square(row, col):
        seen = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                num = board[i][j]
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
        return True

    for i in range(9):
        if not check_row(board[i]):
            return False
        
        if not check_column([board[j][i] for j in range(9)]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_square(i, j):
                return False
    
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
