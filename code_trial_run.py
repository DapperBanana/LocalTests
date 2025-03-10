
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if the matrix is square
    for row in matrix:
        if len(row) != n:
            return False
    
    # Check if all rows have the same sum
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False
    
    # Check if all columns have the same sum
    col_sums = [sum(col) for col in zip(*matrix)]
    if len(set(col_sums)) != 1:
        return False
    
    # Check if the diagonals have the same sum
    diag_sum1 = sum(matrix[i][i] for i in range(n))
    diag_sum2 = sum(matrix[i][n-1-i] for i in range(n))
    if diag_sum1 != diag_sum2 or diag_sum1 != row_sums[0]:
        return False
    
    return True

# Example matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
