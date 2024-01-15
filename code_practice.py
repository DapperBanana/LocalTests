
def is_magic_torus(matrix):
    n = len(matrix)
    
    # Calculate the magic number
    magic_number = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_number:
            return False
    
    # Check columns
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_number:
            return False
    
    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_number:
        return False
    if sum(matrix[i][n-i-1] for i in range(n)) != magic_number:
        return False
    
    return True

# Test the program
matrix1 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]
print(is_magic_torus(matrix1))  # True

matrix2 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
print(is_magic_torus(matrix2))  # False

matrix3 = [
    [2, 9, 6],
    [7, 5, 3],
    [4, 1, 8]
]
print(is_magic_torus(matrix3))  # False
