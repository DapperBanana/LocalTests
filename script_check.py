
def is_magic_square(matrix):
    n = len(matrix)
    magic_num = n * (n**2 + 1) // 2

    # Check rows and columns
    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))
        if row_sum != magic_num or col_sum != magic_num:
            return False

    # Check diagonal sums
    diag_sum1 = sum(matrix[i][i] for i in range(n))
    diag_sum2 = sum(matrix[i][n-1-i] for i in range(n))
    
    if diag_sum1 != magic_num or diag_sum2 != magic_num:
        return False

    return True

# Sample matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
