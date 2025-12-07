using System;

class MatrixMultiplication
{
    static void Main()
    {
        // Define two matrices
        int[,] matrixA = {
            {1, 2, 3},
            {4, 5, 6}
        };

        int[,] matrixB = {
            {7, 8},
            {9, 10},
            {11, 12}
        };

        // Get dimensions
        int rowsA = matrixA.GetLength(0);
        int colsA = matrixA.GetLength(1);
        int rowsB = matrixB.GetLength(0);
        int colsB = matrixB.GetLength(1);

        // Check if multiplication is possible
        if (colsA != rowsB)
        {
            Console.WriteLine("Cannot multiply the matrices: incompatible dimensions.");
            return;
        }

        // Initialize result matrix
        int[,] result = new int[rowsA, colsB];

        // Perform matrix multiplication
        for (int i = 0; i < rowsA; i++)
        {
            for (int j = 0; j < colsB; j++)
            {
                int sum = 0;
                for (int k = 0; k < colsA; k++)
                {
                    sum += matrixA[i, k] * matrixB[k, j];
                }
                result[i, j] = sum;
            }
        }

        // Output the result
        Console.WriteLine("Resultant Matrix:");
        for (int i = 0; i < rowsA; i++)
        {
            for (int j = 0; j < colsB; j++)
            {
                Console.Write(result[i, j] + "\t");
            }
            Console.WriteLine();
        }
    }
}