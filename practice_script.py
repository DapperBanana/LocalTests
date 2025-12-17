using System;

public class MagicTorusChecker
{
    // Checks if the given square matrix is a magic torus
    public static bool IsMagicTorus(int[][] matrix)
    {
        int n = matrix.Length;

        // Ensure matrix is non-empty and square
        if (n == 0 || matrix.Any(row => row.Length != n))
            return false;

        // Calculate the overall sum of main diagonals
        int mainDiagonalSum = 0;
        int secondaryDiagonalSum = 0;
        for (int i = 0; i < n; i++)
        {
            mainDiagonalSum += matrix[i][i];
            secondaryDiagonalSum += matrix[i][n - 1 - i];
        }

        // All row sums, column sums, and diagonals should match mainDiagonalSum
        for (int i = 0; i < n; i++)
        {
            int rowSum = 0;
            int colSum = 0;
            for (int j = 0; j < n; j++)
            {
                rowSum += matrix[i][j];
                colSum += matrix[j][i];
            }

            if (rowSum != mainDiagonalSum || colSum != mainDiagonalSum)
                return false;
        }

        // Verifying the wrap-around diagonals (toroidal diagonals)
        int wrapDiag1Sum = 0;
        int wrapDiag2Sum = 0;
        for (int i = 0; i < n; i++)
        {
            wrapDiag1Sum += matrix[i][(i) % n];
            wrapDiag2Sum += matrix[i][(n - 1 - i + n) % n];
        }

        return (wrapDiag1Sum == mainDiagonalSum) && (wrapDiag2Sum == mainDiagonalSum);
    }

    // Example usage
    public static void Main()
    {
        int[][] matrix = new int[][]
        {
            new int[] { 2, 7, 6 },
            new int[] { 9, 5, 1 },
            new int[] { 4, 3, 8 }
        };

        Console.WriteLine(IsMagicTorus(matrix) ? "The matrix is a magic torus." : "The matrix is not a magic torus.");
    }
}