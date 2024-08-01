
def is_magic_square(matrix):
    n = len(matrix)
    total_sum = sum(matrix[0])
    
    # Check sum of rows
    for row in matrix:
        if sum(row) != total_sum:
            return False
    
    # Check sum of columns
    for i in range(n):
        col_sum = sum(row[i] for row in matrix)
        if col_sum != total_sum:
            return False
    
    # Check sum of diagonals
    diag_sum1 = sum(matrix[i][i] for i in range(n))
    diag_sum2 = sum(matrix[i][n-i-1] for i in range(n))
    if diag_sum1 != total_sum or diag_sum2 != total_sum:
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
