
def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    
    return result

def subtract_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] - b[i][j]
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)


# Example usage
matrix_a = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]]

matrix_b = [[9, 8, 7], 
            [6, 5, 4], 
            [3, 2, 1]]

print("Matrix A:")
print_matrix(matrix_a)

print("\nMatrix B:")
print_matrix(matrix_b)

print("\nAddition:")
result_add = add_matrices(matrix_a, matrix_b)
print_matrix(result_add)

print("\nSubtraction:")
result_sub = subtract_matrices(matrix_a, matrix_b)
print_matrix(result_sub)
