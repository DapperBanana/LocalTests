using System;
using System.Collections.Generic;

public class MazeGeneratorAndSolver
{
    private int width;
    private int height;
    private int[,] maze;
    private bool[,] visited;
    private Random rand = new Random();

    // Directions: Up, Right, Down, Left
    private readonly int[] dx = { 0, 1, 0, -1 };
    private readonly int[] dy = { -1, 0, 1, 0 };

    public MazeGeneratorAndSolver(int width, int height)
    {
        this.width = width;
        this.height = height;
        maze = new int[height, width];
        visited = new bool[height, width];

        // Initialize maze with walls (1)
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                maze[i, j] = 1;

        GenerateMaze(1, 1);
    }

    private void GenerateMaze(int x, int y)
    {
        visited[y, x] = true;
        maze[y, x] = 0; // Path

        int[] dirs = { 0, 1, 2, 3 };
        Shuffle(dirs);

        foreach (int dir in dirs)
        {
            int nx = x + dx[dir] * 2;
            int ny = y + dy[dir] * 2;

            if (nx > 0 && nx < width - 1 && ny > 0 && ny < height - 1)
            {
                if (!visited[ny, nx])
                {
                    // Remove wall between cells
                    maze[y + dy[dir], x + dx[dir]] = 0;
                    GenerateMaze(nx, ny);
                }
            }
        }
    }

    private void Shuffle(int[] array)
    {
        for (int i = array.Length - 1; i > 0; i--)
        {
            int j = rand.Next(i + 1);
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }

    public List<(int x, int y)> SolveMaze(int startX, int startY, int endX, int endY)
    {
        var path = new List<(int x, int y)>();
        var visitedSolve = new bool[height, width];
        if (DFS(startX, startY, endX, endY, path, visitedSolve))
            path.Reverse(); // Path is built backwards
        return path;
    }

    private bool DFS(int x, int y, int endX, int endY, List<(int x, int y)> path, bool[,] visitedSolve)
    {
        if (x == endX && y == endY)
        {
            path.Add((x, y));
            return true;
        }

        visitedSolve[y, x] = true;

        for (int dir = 0; dir < 4; dir++)
        {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx >= 0 && nx < width && ny >= 0 && ny < height)
            {
                if (maze[ny, nx] == 0 && !visitedSolve[ny, nx])
                {
                    if (DFS(nx, ny, endX, endY, path, visitedSolve))
                    {
                        path.Add((x, y));
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public void PrintMaze(List<(int x, int y)> path = null)
    {
        var pathSet = new HashSet<(int x, int y)>(path ?? new List<(int, int)>());

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (pathSet.Contains((x, y)))
                    Console.Write("•");
                else if (maze[y, x] == 0)
                    Console.Write(" ");
                else
                    Console.Write("█");
            }
            Console.WriteLine();
        }
    }

    // Example usage
    public static void Main()
    {
        int width = 21;  // Should be odd for proper maze generation
        int height = 21; // Should be odd for proper maze generation

        var maze = new MazeGeneratorAndSolver(width, height);
        // Define start and end points
        int startX = 1, startY = 1;
        int endX = width - 2, endY = height - 2;

        var path = maze.SolveMaze(startX, startY, endX, endY);
        maze.PrintMaze(path);
    }
}