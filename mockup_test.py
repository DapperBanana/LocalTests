
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
    
    # Check if the sum of the diagonals is the same
    diag1 = sum(matrix[i][i] for i in range(n))
    diag2 = sum(matrix[i][n-i-1] for i in range(n))
    if diag1 != diag2 or diag1 != row_sums[0]:
        return False
    
    return True

# Example matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
