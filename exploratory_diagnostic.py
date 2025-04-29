
def is_magic_square(matrix):
    n = len(matrix)
    
    # Check if rows and columns sum up to the same number
    target_sum = sum(matrix[0])
    for i in range(n):
        if sum(matrix[i]) != target_sum:
            return False
        if sum(matrix[j][i] for j in range(n)) != target_sum:
            return False
    
    # Check if diagonals sum up to the same number
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False
    if sum(matrix[i][n-1-i] for i in range(n)) != target_sum:
        return False
    
    return True

# Test the function
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
if is_magic_square(matrix):
    print("The given matrix is a magic square")
else:
    print("The given matrix is not a magic square")
