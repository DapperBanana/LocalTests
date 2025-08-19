
def is_magic_square(matrix):
    n = len(matrix)
    target_sum = n * (n**2 + 1) // 2

    # Check rows and columns
    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))
        if row_sum != target_sum or col_sum != target_sum:
            return False

    # Check diagonals
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][n-i-1] for i in range(n))
    if diag1_sum != target_sum or diag2_sum != target_sum:
        return False

    return True

# Test the function with a sample matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
