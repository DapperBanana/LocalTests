
def is_symmetric(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    
    if row_len != col_len:
        return False
    
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Example matrix
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if is_symmetric(matrix):
    print("The matrix is symmetric")
else:
    print("The matrix is not symmetric")
