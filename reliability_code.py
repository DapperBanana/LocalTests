
def is_magic_square(matrix):
    n = len(matrix)
    
    # Check if all rows have the same sum
    sum_row = sum(matrix[0])
    for i in range(1, n):
        if sum(matrix[i]) != sum_row:
            return False
        
    # Check if all columns have the same sum
    for j in range(n):
        sum_col = sum(matrix[i][j] for i in range(n))
        if sum_col != sum_row:
            return False
        
    # Check if the diagonals have the same sum
    sum_diag1 = sum(matrix[i][i] for i in range(n))
    sum_diag2 = sum(matrix[n-1-i][i] for i in range(n))
    if sum_diag1 != sum_row or sum_diag2 != sum_row:
        return False
        
    return True

# Test the function with a sample matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The matrix is a magic square.")
else:
    print("The matrix is not a magic square.")
