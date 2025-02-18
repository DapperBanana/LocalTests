
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Calculate expected magic sum
    magic_sum = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
            
    # Check columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
    
    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(matrix[i][n-1-i] for i in range(n)) != magic_sum:
        return False
    
    return True

# Test the program
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_torus(matrix):
    print("The matrix is a magic torus.")
else:
    print("The matrix is not a magic torus.")
