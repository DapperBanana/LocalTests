
def is_valid_sudoku(board):
    # Check each row
    for row in board:
        if not is_valid_row(row):
            return False

    # Check each column
    for i in range(9):
        col = []
        for j in range(9):
            col.append(board[j][i])
        if not is_valid_row(col):
            return False

    # Check each 3x3 subgrid
    for i in range(3):
        for j in range(3):
            subgrid = []
            for k in range(3):
                for l in range(3):
                    subgrid.append(board[3*i + k][3*j + l])
            if not is_valid_row(subgrid):
                return False

    return True

def is_valid_row(row):
    seen = set()
    for num in row:
        if num == '.':
            continue
        if num in seen:
            return False
        seen.add(num)
    return True

# Example Sudoku solution
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

if is_valid_sudoku(board):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
