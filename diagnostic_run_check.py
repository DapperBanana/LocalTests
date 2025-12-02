using System;
using System.Collections.Generic;

class Graph
{
    private readonly Dictionary<int, List<int>> adjacencyList = new Dictionary<int, List<int>>();

    public void AddEdge(int src, int dest)
    {
        if (!adjacencyList.ContainsKey(src))
        {
            adjacencyList[src] = new List<int>();
        }
        adjacencyList[src].Add(dest);
        // If the graph is undirected, uncomment the following lines:
        // if (!adjacencyList.ContainsKey(dest))
        // {
        //     adjacencyList[dest] = new List<int>();
        // }
        // adjacencyList[dest].Add(src);
    }

    public List<int> FindShortestPath(int start, int end)
    {
        var visited = new HashSet<int>();
        var queue = new Queue<List<int>>();

        // Initialize queue with the starting node
        queue.Enqueue(new List<int> { start });
        visited.Add(start);

        while (queue.Count > 0)
        {
            var path = queue.Dequeue();
            var node = path[path.Count - 1];

            if (node == end)
            {
                return path; // Shortest path found
            }

            if (adjacencyList.ContainsKey(node))
            {
                foreach (var neighbor in adjacencyList[node])
                {
                    if (!visited.Contains(neighbor))
                    {
                        visited.Add(neighbor);
                        var newPath = new List<int>(path) { neighbor };
                        queue.Enqueue(newPath);
                    }
                }
            }
        }
        return null; // No path found
    }
}

// Example usage
class Program
{
    static void Main()
    {
        var graph = new Graph();

        // Add edges
        graph.AddEdge(1, 2);
        graph.AddEdge(1, 3);
        graph.AddEdge(2, 4);
        graph.AddEdge(3, 4);
        graph.AddEdge(4, 5);
        graph.AddEdge(2, 5);

        var path = graph.FindShortestPath(1, 5);
        if (path != null)
        {
            Console.WriteLine("Shortest path: " + string.Join(" -> ", path));
        }
        else
        {
            Console.WriteLine("No path found");
        }
    }
}