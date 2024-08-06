
def check_row(board, row):
    return len(set(board[row])) == len(board[row])

def check_col(board, col):
    return len(set(row[col] for row in board)) == len(board)

def check_square(board, row, col):
    square_nums = set()
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    
    for i in range(start_row, start_row+3):
        for j in range(start_col, start_col+3):
            if board[i][j] in square_nums:
                return False
            square_nums.add(board[i][j])
    
    return True

def is_valid_sudoku(board):
    for i in range(9):
        if not (check_row(board, i) and check_col(board, i)):
            return False
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_square(board, i, j):
                return False
            
    return True

# Test the program with an example Sudoku solution
board = [
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

if is_valid_sudoku(board):
    print("The given Sudoku solution is valid.")
else:
    print("The given Sudoku solution is not valid.")
