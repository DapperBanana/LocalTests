
def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = n * (n**2 + 1) // 2

    # Check rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Check columns
    for i in range(n):
        col_sum = sum(matrix[j][i] for j in range(n))
        if col_sum != magic_sum:
            return False

    # Check diagonals
    diag_sum1 = sum(matrix[i][i] for i in range(n))
    diag_sum2 = sum(matrix[i][n-i-1] for i in range(n))

    if diag_sum1 != magic_sum or diag_sum2 != magic_sum:
        return False

    return True

# Test the function
matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
if is_magic_square(matrix):
    print("The matrix is a magic square")
else:
    print("The matrix is not a magic square")
