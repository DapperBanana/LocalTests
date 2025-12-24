using System;

class MatrixMultiplication
{
    static void Main()
    {
        // Example matrices
        int[,] A = { { 1, 2, 3 }, { 4, 5, 6 } };
        int[,] B = { { 7, 8 }, { 9, 10 }, { 11, 12 } };

        // Validate matrices dimensions
        int aRows = A.GetLength(0);
        int aCols = A.GetLength(1);
        int bRows = B.GetLength(0);
        int bCols = B.GetLength(1);

        if (aCols != bRows)
        {
            Console.WriteLine("Cannot multiply matrices: incompatible dimensions.");
            return;
        }

        int[,] result = new int[aRows, bCols];

        // Perform matrix multiplication
        for (int i = 0; i < aRows; i++)
        {
            for (int j = 0; j < bCols; j++)
            {
                int sum = 0;
                for (int k = 0; k < aCols; k++)
                {
                    sum += A[i, k] * B[k, j];
                }
                result[i, j] = sum;
            }
        }

        // Output result
        Console.WriteLine("Resultant Matrix:");
        for (int i = 0; i < aRows; i++)
        {
            for (int j = 0; j < bCols; j++)
            {
                Console.Write(result[i, j] + "\t");
            }
            Console.WriteLine();
        }
    }
}