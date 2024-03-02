
def add_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

def subtract_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    
    return result

# Test the functions
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result_addition = add_matrices(matrix1, matrix2)
result_subtraction = subtract_matrices(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
    print(row)
    
print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nMatrix Addition:")
for row in result_addition:
    print(row)
    
print("\nMatrix Subtraction:")
for row in result_subtraction:
    print(row)
