
def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    
    return True

# Example matrix
matrix = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
