
def add_matrices(matrix1, matrix2):
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result.append([elem1 + elem2 for elem1, elem2 in zip(row1, row2)])
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result.append([elem1 - elem2 for elem1, elem2 in zip(row1, row2)])
    return result

def main():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("Matrix 2:")
    for row in matrix2:
        print(row)

    print("Matrix sum:")
    result = add_matrices(matrix1, matrix2)
    for row in result:
        print(row)

    print("Matrix difference:")
    result = subtract_matrices(matrix1, matrix2)
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
