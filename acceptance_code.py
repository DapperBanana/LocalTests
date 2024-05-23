
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
            subgrid = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            if not is_valid_row(subgrid):
                return False
    
    return True

def is_valid_row(row):
    seen = set()
    for num in row:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True

# Example Sudoku board
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
    print("Sudoku solution is valid")
else:
    print("Sudoku solution is not valid")
