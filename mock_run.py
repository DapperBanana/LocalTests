
def is_magic_square(matrix):
    # Check if all rows, columns and diagonals have the same sum
    n = len(matrix)
    target_sum = sum(matrix[0])

    # Check rows
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # Check columns
    for j in range(n):
        col_sum = sum(row[j] for row in matrix)
        if col_sum != target_sum:
            return False

    # Check diagonal 1
    diagonal_1_sum = sum(matrix[i][i] for i in range(n))
    if diagonal_1_sum != target_sum:
        return False

    # Check diagonal 2
    diagonal_2_sum = sum(matrix[i][n-1-i] for i in range(n))
    if diagonal_2_sum != target_sum:
        return False

    return True

# Test the function with a sample matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The matrix is a magic square")
else:
    print("The matrix is not a magic square")
