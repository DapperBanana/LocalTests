
def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_set(row):
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False

    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grid = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            if not is_valid_set(grid):
                return False

    return True

def is_valid_set(nums):
    seen = set()
    for num in nums:
        if num != 0:
            if num in seen:
                return False
            seen.add(num)
    return True

# Example Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if is_valid_sudoku(board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
