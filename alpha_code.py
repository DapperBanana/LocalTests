
def validate_sudoku(board):
    # Check rows
    for row in board:
        if sorted(row) != list(range(1, 10)):
            return False

    # Check columns
    for col in range(9):
        if sorted([row[col] for row in board]) != list(range(1, 10)):
            return False

    # Check 3x3 subgrids
    for i in range(3):
        for j in range(3):
            subgrid = [board[x][y] for x in range(i*3, (i+1)*3) for y in range(j*3, (j+1)*3)]
            if sorted(subgrid) != list(range(1, 10)):
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

if validate_sudoku(board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
