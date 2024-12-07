
def is_magic_square(matrix):
    n = len(matrix)

    # Check if all rows have same sum
    sum_rows = [sum(row) for row in matrix]
    if len(set(sum_rows)) != 1:
        return False

    # Check if all columns have same sum
    sum_cols = [sum(col) for col in zip(*matrix)]
    if len(set(sum_cols)) != 1:
        return False

    # Check if both diagonals have same sum
    diagonal1 = [matrix[i][i] for i in range(n)]
    diagonal2 = [matrix[i][n-i-1] for i in range(n)]
    if sum(diagonal1) != sum(diagonal2) or sum(diagonal1) != sum_rows[0]:
        return False

    return True

# Test the program with a sample matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
