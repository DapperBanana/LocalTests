using System;
using System.Collections.Generic;

class MazeSolver
{
    static char[,] maze = {
        { '#', '#', '#', '#', '#', '#', '#', '#', '#' },
        { '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#' },
        { '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#' },
        { '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#' },
        { '#', ' ', '#', '#', '#', ' ', '#', ' ', '#' },
        { '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#' },
        { '#', '#', '#', ' ', '#', '#', '#', ' ', '#' },
        { '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' },
        { '#', '#', '#', '#', '#', '#', '#', '#', '#' }
    };

    static int rows = maze.GetLength(0);
    static int cols = maze.GetLength(1);

    // Start and end positions
    static (int, int) start = (1,1);
    static (int, int) end = (7,7);

    static bool[,] visited = new bool[rows, cols];

    // Directions: up, right, down, left
    static int[] dirRow = { -1, 0, 1, 0 };
    static int[] dirCol = { 0, 1, 0, -1 };

    static void Main()
    {
        List<(int, int)> path = new List<(int, int)>();
        if (SolveMaze(start.Item1, start.Item2, path))
        {
            Console.WriteLine("Path to the exit:");
            foreach (var position in path)
            {
                Console.WriteLine($"({position.Item1}, {position.Item2})");
                // Mark the path in the maze
                if (maze[position.Item1, position.Item2] == ' ')
                {
                    maze[position.Item1, position.Item2] = '.';
                }
            }

            // Print the maze with path
            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < cols; j++)
                {
                    Console.Write(maze[i, j]);
                }
                Console.WriteLine();
            }
        }
        else
        {
            Console.WriteLine("No path found.");
        }
    }

    static bool SolveMaze(int r, int c, List<(int, int)> path)
    {
        // Check boundaries and visited
        if (r < 0 || r >= rows || c < 0 || c >= cols || maze[r, c] == '#' || visited[r, c])
            return false;

        // Add current position to path
        path.Add((r, c));
        visited[r, c] = true;

        // Check if end is reached
        if (r == end.Item1 && c == end.Item2)
            return true;

        // Explore neighbors
        for (int i = 0; i < 4; i++)
        {
            int newRow = r + dirRow[i];
            int newCol = c + dirCol[i];

            if (SolveMaze(newRow, newCol, path))
                return true;
        }

        // Backtrack
        path.RemoveAt(path.Count - 1);
        return false;
    }
}