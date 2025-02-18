
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# Test the functions
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Addition
result_addition = add_matrices(matrix1, matrix2)
print("Addition Result:")
for row in result_addition:
    print(row)

# Subtraction
result_subtraction = subtract_matrices(matrix1, matrix2)
print("\nSubtraction Result:")
for row in result_subtraction:
    print(row)
