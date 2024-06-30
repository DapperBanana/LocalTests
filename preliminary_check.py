
def is_valid_sudoku(board):
    def is_valid_row(row):
        return len(row) == len(set(row))  # Check if row has no duplicates
    
    def is_valid_col(col):
        return len(col) == len(set(col))  # Check if column has no duplicates
    
    def is_valid_square(square):
        flat_square = [num for sublist in square for num in sublist]
        return len(flat_square) == len(set(flat_square))  # Check if 3x3 square has no duplicates
    
    rows = board
    cols = [[board[j][i] for j in range(9)] for i in range(9)]
    squares = [[board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] for j in range(9)] for i in range(9)]
    
    for row in rows:
        if not is_valid_row(row):
            return False
        
    for col in cols:
        if not is_valid_col(col):
            return False
        
    for square in squares:
        if not is_valid_square(square):
            return False
        
    return True

# Test the program
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
    print("Valid Sudoku Solution")
else:
    print("Invalid Sudoku Solution")
