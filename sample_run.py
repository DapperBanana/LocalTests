// Basic text-based maze solver using DFS
using System;
using System.Collections.Generic;

class MazeSolver
{
    // Maze representation (0: path, 1: wall)
    static int[,] maze = {
        {0, 1, 0, 0, 0},
        {0, 1, 0, 1, 0},
        {0, 0, 0, 1, 0},
        {1, 1, 0, 1, 0},
        {0, 0, 0, 0, 0}
    };

    static int rows = maze.GetLength(0);
    static int cols = maze.GetLength(1);
    static bool[,] visited = new bool[rows, cols];
    static List<(int, int)> path = new List<(int, int)>();

    static (int, int) start = (0, 0);
    static (int, int) end = (4, 4);

    static void Main()
    {
        if (SolveMaze(start.Item1, start.Item2))
        {
            Console.WriteLine("Path found:");
            foreach (var step in path)
            {
                Console.WriteLine($"({step.Item1}, {step.Item2})");
            }
        }
        else
        {
            Console.WriteLine("No path found.");
        }
    }

    static bool SolveMaze(int row, int col)
    {
        if (row < 0 || col < 0 || row >= rows || col >= cols)
            return false;
        if (maze[row, col] == 1 || visited[row, col])
            return false;

        visited[row, col] = true;
        path.Add((row, col));

        if (row == end.Item1 && col == end.Item2)
            return true;

        // Explore neighbors: up, right, down, left
        int[] dRow = {-1, 0, 1, 0};
        int[] dCol = {0, 1, 0, -1};

        for (int i = 0; i < 4; i++)
        {
            int newRow = row + dRow[i];
            int newCol = col + dCol[i];

            if (SolveMaze(newRow, newCol))
                return true;
        }

        // Backtrack
        path.RemoveAt(path.Count - 1);
        return false;
    }
}