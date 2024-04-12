
def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element for row {i+1} and column {j+1}: "))
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: ")

print("Enter Matrix 1:")
matrix1 = create_matrix(rows, cols)

print("Enter Matrix 2:")
matrix2 = create_matrix(rows, cols)

print("Matrix 1: ")
for row in matrix1:
    print(row)

print("Matrix 2: ")
for row in matrix2:
    print(row)

addition_result = add_matrices(matrix1, matrix2)
print("Matrix Addition Result: ")
for row in addition_result:
    print(row)

subtraction_result = subtract_matrices(matrix1, matrix2)
print("Matrix Subtraction Result: ")
for row in subtraction_result:
    print(row)
