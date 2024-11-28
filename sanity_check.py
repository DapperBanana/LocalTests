
def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(i, cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    
    return True

# Example usage
matrix1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matrix2 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 6, 7]
]

if is_symmetric(matrix1):
    print("Matrix 1 is symmetric")
else:
    print("Matrix 1 is not symmetric")

if is_symmetric(matrix2):
    print("Matrix 2 is symmetric")
else:
    print("Matrix 2 is not symmetric")
