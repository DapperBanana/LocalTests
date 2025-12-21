using System;
using System.Collections.Generic;

class MazeSolver
{
    static char[,] maze = {
        {'#', '#', '#', '#', '#', '#', '#', '#', '#'},
        {'#', 'S', ' ', ' ', '#', ' ', ' ', ' ', '#'},
        {'#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'},
        {'#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'},
        {'#', ' ', '#', '#', '#', ' ', '#', ' ', '#'},
        {'#', ' ', ' ', ' ', '#', ' ', ' ', 'E', '#'},
        {'#', '#', '#', '#', '#', '#', '#', '#', '#'}
    };

    static int rows = maze.GetLength(0);
    static int cols = maze.GetLength(1);
    static bool[,] visited = new bool[rows, cols];

    static void Main()
    {
        (int, int) start = FindPoint('S');
        (int, int) end = FindPoint('E');

        if (start == (-1, -1) || end == (-1, -1))
        {
            Console.WriteLine("Start or End point not found in the maze.");
            return;
        }

        if (SolveMaze(start.Item1, start.Item2))
        {
            Console.WriteLine("Maze solved! Path marked with '.'");
            PrintMaze();
        }
        else
        {
            Console.WriteLine("No path found in the maze.");
        }
    }

    static (int, int) FindPoint(char point)
    {
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (maze[r, c] == point)
                    return (r, c);
            }
        }
        return (-1, -1);
    }

    static bool SolveMaze(int r, int c)
    {
        if (r < 0 || c < 0 || r >= rows || c >= cols)
            return false;

        if (maze[r, c] == '#'
            || visited[r, c])
            return false;

        if (maze[r, c] == 'E')
            return true;

        visited[r, c] = true;

        // Explore neighbors: Up, Right, Down, Left
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};

        for (int i = 0; i < 4; i++)
        {
            int newR = r + dr[i];
            int newC = c + dc[i];

            if (SolveMaze(newR, newC))
            {
                if (maze[r, c] == ' ')
                    maze[r, c] = '.'; // Mark path
                return true;
            }
        }

        return false;
    }

    static void PrintMaze()
    {
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                Console.Write(maze[r, c]);
            }
            Console.WriteLine();
        }
    }
}