
def is_magic_square(matrix):
    n = len(matrix)
    
    # calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # check if the sums of each row, column, and diagonal are equal to the target sum
    for i in range(n):
        if sum(matrix[i]) != target_sum:
            return False
        
        col_sum = sum([matrix[j][i] for j in range(n)])
        if col_sum != target_sum:
            return False
    
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][n-1-i] for i in range(n))
    
    if diag1_sum != target_sum or diag2_sum != target_sum:
        return False
    
    return True

# Test the function with an example matrix
matrix = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
if is_magic_square(matrix):
    print("The matrix is a magic square")
else:
    print("The matrix is not a magic square")
