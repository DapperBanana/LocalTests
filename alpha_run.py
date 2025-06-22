
def is_magic_torus(matrix):
    n = len(matrix)
    magic_number = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_number:
            return False
    
    # Check columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_number:
            return False
    
    # Check main diagonal
    if sum(matrix[i][i] for i in range(n)) != magic_number:
        return False
    
    # Check anti-diagonal
    if sum(matrix[i][n-i-1] for i in range(n)) != magic_number:
        return False
    
    return True

# Test the program
matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")
