using System;
using System.Collections.Generic;

class Maze
{
    private int width, height;
    private int[,] maze;
    private bool[,] visited;
    private Random rand = new Random();

    // Maze cell representation:
    // 0: wall, 1: passage
    public Maze(int width, int height)
    {
        this.width = width * 2 + 1;
        this.height = height * 2 + 1;
        maze = new int[this.width, this.height];
        visited = new bool[this.width, this.height];

        // Initialize maze with walls
        for(int i = 0; i < this.width; i++)
            for(int j = 0; j < this.height; j++)
                maze[i, j] = 0;

        GenerateMaze(1,1);
    }

    private void GenerateMaze(int x, int y)
    {
        visited[x, y] = true;
        maze[x, y] = 1;

        int[] directions = { 0, 1, 2, 3 };
        Shuffle(directions);

        foreach(int direction in directions)
        {
            int nx = x, ny = y;
            switch(direction)
            {
                case 0: nx = x + 2; break; // Down
                case 1: nx = x - 2; break; // Up
                case 2: ny = y + 2; break; // Right
                case 3: ny = y - 2; break; // Left
            }

            if(nx > 0 && nx < width - 1 && ny > 0 && ny < height - 1 && !visited[nx, ny])
            {
                maze[(x + nx)/2, (y + ny)/2] = 1; // Remove wall between cells
                GenerateMaze(nx, ny);
            }
        }
    }

    private void Shuffle(int[] array)
    {
        for(int i = array.Length - 1; i > 0; i--)
        {
            int j = rand.Next(i + 1);
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }

    public bool SolveMaze()
    {
        return DFS(1,1);
    }

    private bool DFS(int x, int y)
    {
        if(x == width - 2 && y == height - 2)
        {
            maze[x, y] = 2; // Mark path
            return true;
        }

        if(x < 0 || y < 0 || x >= width || y >= height || maze[x, y] == 0 || maze[x, y] == 3)
            return false;

        maze[x, y] = 3; // Mark visited

        int[] dx = { 0, 1, 0, -1 };
        int[] dy = { 1, 0, -1, 0 };

        for(int dir = 0; dir < 4; dir++)
        {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if(DFS(nx, ny))
            {
                maze[x, y] = 2; // Mark path on solution
                return true;
            }
        }
        return false;
    }

    public void PrintMaze()
    {
        for(int y = 0; y < this.height; y++)
        {
            for(int x = 0; x < this.width; x++)
            {
                if(maze[x, y] == 0)
                    Console.Write("#");
                else if(maze[x, y] == 2)
                    Console.Write(".");
                else
                    Console.Write(" ");
            }
            Console.WriteLine();
        }
    }
}

class Program
{
    static void Main()
    {
        int mazeWidth = 10;
        int mazeHeight = 10;

        Maze maze = new Maze(mazeWidth, mazeHeight);
        Console.WriteLine("Generated Maze:");
        maze.PrintMaze();

        if(maze.SolveMaze())
        {
            Console.WriteLine("\nSolution Path:");
            maze.PrintMaze();
        }
        else
        {
            Console.WriteLine("No solution found!");
        }
    }
}