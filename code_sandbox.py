
def is_magic_square(matrix):
    n = len(matrix)
    
    # Check if all rows have the same sum
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False
    
    # Check if all columns have the same sum
    col_sums = [sum(col) for col in zip(*matrix)]
    if len(set(col_sums)) != 1:
        return False
    
    # Check if both diagonals have the same sum
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][n-1-i] for i in range(n))
    if diag1_sum != diag2_sum or diag1_sum != row_sums[0]:
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
