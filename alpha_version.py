
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check if all rows have the same sum
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Check if all columns have the same sum
    for i in range(n):
        col_sum = sum(matrix[j][i] for j in range(n))
        if col_sum != target_sum:
            return False
            
    # Check if the sum of the diagonals are the same
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    anti_diag_sum = sum(matrix[i][n-i-1] for i in range(n))
    
    if main_diag_sum != target_sum or anti_diag_sum != target_sum:
        return False
        
    return True

# Example matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The matrix is a magic square")
else:
    print("The matrix is not a magic square")
