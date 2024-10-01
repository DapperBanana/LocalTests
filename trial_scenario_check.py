
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if all rows have the same sum
    row_sum = sum(matrix[0])
    for row in matrix[1:]:
        if sum(row) != row_sum:
            return False
    
    # Check if all columns have the same sum
    col_sums = [sum(col) for col in zip(*matrix)]
    if len(set(col_sums)) != 1:
        return False
    
    # Check if the diagonal sums are the same
    diag_sum1 = sum(matrix[i][i] for i in range(n))
    diag_sum2 = sum(matrix[i][n-1-i] for i in range(n))
    
    return row_sum == col_sums[0] == diag_sum1 == diag_sum2

# Test the function
matrix = [
    [23, 28, 21],
    [22, 24, 26],
    [27, 20, 25]
]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
