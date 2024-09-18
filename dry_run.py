
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check if all row sums are equal to the target sum
    for row in matrix:
        if sum(row) != target_sum:
            return False
            
    # Check if all column sums are equal to the target sum
    for i in range(n):
        col_sum = sum(matrix[j][i] for j in range(n))
        if col_sum != target_sum:
            return False
            
    # Check if the sums of the two diagonals are equal to the target sum
    d1_sum = sum(matrix[i][i] for i in range(n))
    d2_sum = sum(matrix[i][n-i-1] for i in range(n))
    
    if d1_sum != target_sum or d2_sum != target_sum:
        return False
        
    return True

# Example usage
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The matrix is a magic square.")
else:
    print("The matrix is not a magic square.")
