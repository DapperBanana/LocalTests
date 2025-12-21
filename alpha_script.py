using System;
using System.Collections.Generic;

public class Graph
{
    private Dictionary<int, List<int>> adjacencyList;

    public Graph()
    {
        adjacencyList = new Dictionary<int, List<int>>();
    }

    public void AddEdge(int source, int destination)
    {
        if (!adjacencyList.ContainsKey(source))
            adjacencyList[source] = new List<int>();
        adjacencyList[source].Add(destination);

        // If the graph is undirected, uncomment the following:
        // if (!adjacencyList.ContainsKey(destination))
        //     adjacencyList[destination] = new List<int>();
        // adjacencyList[destination].Add(source);
    }

    public List<int> ShortestPath(int start, int goal)
    {
        var visited = new HashSet<int>();
        var queue = new Queue<List<int>>();

        queue.Enqueue(new List<int> { start });
        visited.Add(start);

        while (queue.Count > 0)
        {
            var path = queue.Dequeue();
            int current = path[path.Count - 1];

            if (current == goal)
                return path;

            if (adjacencyList.ContainsKey(current))
            {
                foreach (var neighbor in adjacencyList[current])
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

// Example usage:
class Program
{
    static void Main()
    {
        var graph = new Graph();
        graph.AddEdge(1, 2);
        graph.AddEdge(1, 3);
        graph.AddEdge(2, 4);
        graph.AddEdge(3, 4);
        graph.AddEdge(4, 5);

        int start = 1;
        int goal = 5;
        var shortestPath = graph.ShortestPath(start, goal);

        if (shortestPath != null)
        {
            Console.WriteLine("Shortest path: " + string.Join(" -> ", shortestPath));
        }
        else
        {
            Console.WriteLine("No path found between " + start + " and " + goal);
        }
    }
}