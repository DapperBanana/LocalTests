
def is_valid_sudoku(board):
    def is_valid_row(arr):
        return len(set(arr)) == 9 and all(num in range(1, 10) for num in arr)

    def is_valid_col(arr):
        return len(set(arr)) == 9 and all(num in range(1, 10) for num in arr)

    def is_valid_box(arr):
        return len(set(arr)) == 9 and all(num in range(1, 10) for num in arr)

    for row in board:
        if not is_valid_row(row):
            return False

    for col in zip(*board):
        if not is_valid_col(col):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_box(box):
                return False

    return True

# Example Sudoku solution
sudoku = [
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

if is_valid_sudoku(sudoku):
    print("Valid Sudoku solution")
else:
    print("Invalid Sudoku solution")
