public class MatrixReversal
{
    public static int[,] ReverseMatrix(int[,] matrix)
    {
        int rows = matrix.GetLength(0);
        int cols = matrix.GetLength(1);
        int[,] reversedMatrix = new int[rows, cols];

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                // Map each element to its reversed position
                reversedMatrix[rows - 1 - i, cols - 1 - j] = matrix[i, j];
            }
        }

        return reversedMatrix;
    }
}