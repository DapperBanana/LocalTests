
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if all rows have equal sum
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False
    
    # Check if all columns have equal sum
    col_sums = [sum(col) for col in zip(*matrix)]
    if len(set(col_sums)) != 1:
        return False
    
    # Check if diagonals have equal sum
    diagonal_sum1 = sum(matrix[i][i] for i in range(n))
    diagonal_sum2 = sum(matrix[i][n-1-i] for i in range(n))
    if diagonal_sum1 != row_sums[0] or diagonal_sum2 != row_sums[0]:
        return False
    
    return True

# Sample matrix
matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

if is_magic_torus(matrix):
    print("The matrix is a magic torus")
else:
    print("The matrix is not a magic torus")
