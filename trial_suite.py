
def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
            
    # Check columns
    for i in range(n):
        if sum(matrix[j][i] for j in range(n)) != magic_sum:
            return False
            
    # Check diagonal 1
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
        
    # Check diagonal 2
    if sum(matrix[i][n-i-1] for i in range(n)) != magic_sum:
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
