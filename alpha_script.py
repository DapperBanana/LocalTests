
def is_magic_square(matrix):
    # Check if the matrix is a square matrix
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check if the sums of all rows, columns, and diagonals are equal to the target sum
    for i in range(n):
        if sum(matrix[i]) != target_sum:
            return False
        
        if sum(matrix[j][i] for j in range(n)) != target_sum:
            return False
    
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False
    
    if sum(matrix[i][n-i-1] for i in range(n)) != target_sum:
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
