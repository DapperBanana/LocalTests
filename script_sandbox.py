// Note: The following is a C# implementation of a basic content-based recommendation system.
// It simulates recommendations based on item features and a user's preferred features.

using System;
using System.Collections.Generic;
using System.Linq;

class ContentBasedRecommender
{
    // Define an Item class with ID and feature vector
    class Item
    {
        public int Id { get; set; }
        public double[] Features { get; set; }

        public Item(int id, double[] features)
        {
            Id = id;
            Features = features;
        }
    }

    // Sample dataset of items
    static List<Item> items = new List<Item>
    {
        new Item(1, new double[] {1.0, 0.0, 3.0}),
        new Item(2, new double[] {0.0, 2.0, 1.0}),
        new Item(3, new double[] {3.0, 1.0, 0.0}),
        new Item(4, new double[] {0.0, 0.0, 4.0}),
        new Item(5, new double[] {2.0, 2.0, 2.0})
    };

    // User's preferred features
    static double[] userPreferences = new double[] {1.0, 1.0, 1.0};

    static void Main()
    {
        Console.WriteLine("Content-Based Recommendation System");
        Console.WriteLine("User preferences: [{0}]", string.Join(", ", userPreferences));
        Console.WriteLine("Recommending items based on similarity...\n");

        // Calculate similarity scores
        var scoredItems = items.Select(item => new
        {
            ItemId = item.Id,
            Score = CosineSimilarity(userPreferences, item.Features)
        })
        .OrderByDescending(x => x.Score)
        .ToList();

        // Recommend top items
        int topK = 3; // Number of recommendations
        Console.WriteLine($"Top {topK} recommendations:");
        for (int i = 0; i < Math.Min(topK, scoredItems.Count); i++)
        {
            Console.WriteLine($"Item {scoredItems[i].ItemId} with similarity score: {scoredItems[i].Score:F3}");
        }
    }

    // Compute cosine similarity between two vectors
    static double CosineSimilarity(double[] vecA, double[] vecB)
    {
        double dotProduct = 0.0;
        double normA = 0.0;
        double normB = 0.0;

        for (int i = 0; i < vecA.Length; i++)
        {
            dotProduct += vecA[i] * vecB[i];
            normA += vecA[i] * vecA[i];
            normB += vecB[i] * vecB[i];
        }

        if (normA == 0 || normB == 0)
            return 0;

        return dotProduct / (Math.Sqrt(normA) * Math.Sqrt(normB));
    }
}