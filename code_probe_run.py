using System;
using System.Collections.Generic;

class MazeGeneratorAndSolver
{
    static int width = 20;
    static int height = 10;
    static int[,] maze = new int[width, height];
    static bool[,] visited = new bool[width, height];
    static Random rand = new Random();

    static void Main()
    {
        GenerateMaze();
        Console.WriteLine("Generated Maze:");
        PrintMaze();

        if (SolveMaze(0, 0))
        {
            Console.WriteLine("\nMaze Solution:");
            PrintMaze(solution:true);
        }
        else
        {
            Console.WriteLine("No solution found.");
        }
    }

    // Generate maze using recursive backtracking
    static void GenerateMaze()
    {
        // Initialize maze with walls
        for (int x = 0; x < width; x++)
            for (int y = 0; y < height; y++)
                maze[x, y] = 1; // Wall

        CarvePath(0, 0);
    }

    static void CarvePath(int x, int y)
    {
        visited[x, y] = true;
        maze[x, y] = 0; // Path

        var directions = new List<(int dx, int dy)> { (0, -1), (1, 0), (0, 1), (-1, 0) };
        Shuffle(directions);

        foreach (var (dx, dy) in directions)
        {
            int nx = x + dx * 2;
            int ny = y + dy * 2;
            if (IsInBounds(nx, ny) && !visited[nx, ny])
            {
                maze[x + dx, y + dy] = 0; // Remove wall between cells
                CarvePath(nx, ny);
            }
        }
    }

    static bool IsInBounds(int x, int y)
    {
        return x >= 0 && x < width && y >= 0 && y < height;
    }

    static void Shuffle<T>(IList<T> list)
    {
        for (int i = 0; i < list.Count; i++)
        {
            int j = rand.Next(i, list.Count);
            T temp = list[i];
            list[i] = list[j];
            list[j] = temp;
        }
    }

    static Stack<(int x, int y)> pathStack = new Stack<(int x, int y)>();
    static bool[,] solutionVisited = new bool[width, height];
    static bool solutionFound = false;
    static List<(int x, int y)> solutionPath = new List<(int, int)>();

    static bool SolveMaze(int x, int y)
    {
        if (!IsInBounds(x, y) || maze[x, y] == 1 || solutionVisited[x, y])
            return false;

        solutionVisited[x, y] = true;
        pathStack.Push((x, y));

        if (x == width - 1 && y == height - 1)
        {
            solutionFound = true;
            solutionPath = new List<(int, int)>(pathStack);
            return true;
        }

        var directions = new List<(int dx, int dy)> { (0, -1), (1, 0), (0, 1), (-1, 0) };
        foreach (var (dx, dy) in directions)
        {
            int nx = x + dx;
            int ny = y + dy;
            if (SolveMaze(nx, ny))
                return true;
        }

        pathStack.Pop();
        return false;
    }

    static void PrintMaze(bool solution = false)
    {
        var displayPath = new bool[width, height];
        if (solution)
        {
            foreach (var (x, y) in solutionPath)
                displayPath[x, y] = true;
        }

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (displayPath[x, y])
                {
                    Console.Write("*"); // Path in solution
                }
                else if (maze[x, y] == 0)
                {
                    Console.Write(" "); // Path
                }
                else
                {
                    Console.Write("#"); // Wall
                }
            }
            Console.WriteLine();
        }
    }
}