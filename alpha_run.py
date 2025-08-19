
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Check if the matrix is square
    if n != len(matrix[0]):
        return False
    
    # Calculate the expected magic sum
    magic_sum = n * (n**2 + 1) // 2
    
    # Check if all rows have the same sum
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
    # Check if all columns have the same sum
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
    
    # Check if the diagonals have the same sum
    diagonal_sum1 = sum(matrix[i][i] for i in range(n))
    diagonal_sum2 = sum(matrix[i][n-i-1] for i in range(n))
    
    if diagonal_sum1 != magic_sum or diagonal_sum2 != magic_sum:
        return False
    
    return True

# Example matrix
matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
