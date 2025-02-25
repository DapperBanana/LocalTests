
def check_magic_torus(matrix):
    n = len(matrix)
    
    # Checking rows
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False
    
    # Checking columns
    col_sums = [sum(col) for col in zip(*matrix)]
    if len(set(col_sums)) != 1:
        return False
    
    # Checking diagonals
    diag_sum1 = sum(matrix[i][i] for i in range(n))
    diag_sum2 = sum(matrix[i][n-i-1] for i in range(n))
    if diag_sum1 != row_sums[0] or diag_sum2 != row_sums[0]:
        return False
    
    return True

# Example matrix
matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

if check_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
