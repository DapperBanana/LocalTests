using System;
using System.Collections.Generic;

public class Graph
{
    private int vertices;
    private List<List<(int, int)>> adj;

    public Graph(int v)
    {
        vertices = v;
        adj = new List<List<(int, int)>>(v);
        for (int i = 0; i < v; i++)
        {
            adj.Add(new List<(int, int)>());
        }
    }

    public void AddEdge(int u, int v, int weight)
    {
        adj[u].Add((v, weight));
        // If undirected graph, also add the reverse edge
        // adj[v].Add((u, weight));
    }

    public int[] Dijkstra(int start)
    {
        int[] dist = new int[vertices];
        bool[] sptSet = new bool[vertices];

        // Initialize distances with infinity
        for (int i = 0; i < vertices; i++)
        {
            dist[i] = int.MaxValue;
        }
        dist[start] = 0;

        for (int count = 0; count < vertices - 1; count++)
        {
            int u = MinDistance(dist, sptSet);
            sptSet[u] = true;

            foreach (var (v, weight) in adj[u])
            {
                if (!sptSet[v] && dist[u] != int.MaxValue && dist[u] + weight < dist[v])
                {
                    dist[v] = dist[u] + weight;
                }
            }
        }

        return dist;
    }

    private int MinDistance(int[] dist, bool[] sptSet)
    {
        int min = int.MaxValue;
        int minIndex = -1;

        for (int v = 0; v < vertices; v++)
        {
            if (!sptSet[v] && dist[v] <= min)
            {
                min = dist[v];
                minIndex = v;
            }
        }
        return minIndex;
    }
}

// Example usage
class Program
{
    static void Main()
    {
        int V = 5;
        Graph g = new Graph(V);
        g.AddEdge(0, 1, 09);
        g.AddEdge(0, 4, 20);
        g.AddEdge(1, 2, 4);
        g.AddEdge(1, 3, 11);
        g.AddEdge(2, 3, 1);
        g.AddEdge(3, 4, 7);

        int startVertex = 0;
        int[] distances = g.Dijkstra(startVertex);

        Console.WriteLine("Vertex\tDistance from Source");
        for (int i = 0; i < V; i++)
        {
            Console.WriteLine($"{i}\t{distances[i]}");
        }
    }
}