
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

def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    result_add = add_matrices(matrix1, matrix2)
    result_subtract = subtract_matrices(matrix1, matrix2)

    print("\nAddition of matrices:")
    for row in result_add:
        print(row)

    print("\nSubtraction of matrices:")
    for row in result_subtract:
        print(row)

if __name__ == "__main__":
    main()
