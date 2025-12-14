using System;
using System.Collections.Generic;

class Recipe
{
    public string Name { get; set; }
    public List<string> Ingredients { get; set; }
    public string Cuisine { get; set; }

    public Recipe(string name, List<string> ingredients, string cuisine)
    {
        Name = name;
        Ingredients = ingredients;
        Cuisine = cuisine;
    }
}

class RecipeRecommendationSystem
{
    static List<Recipe> recipes = new List<Recipe>()
    {
        new Recipe("Spaghetti Carbonara", new List<string> { "spaghetti", "egg", "cheese", "bacon" }, "Italian"),
        new Recipe("Chicken Tacos", new List<string> { "chicken", "tortilla", "lettuce", "cheese" }, "Mexican"),
        new Recipe("Vegetable Stir Fry", new List<string> { "broccoli", "carrot", "bell pepper", "soy sauce" }, "Chinese"),
        new Recipe("Pancakes", new List<string> { "flour", "egg", "milk", "sugar" }, "American"),
        new Recipe("Sushi Roll", new List<string> { "rice", "nori", "fish", "avocado" }, "Japanese")
    };

    static void Main()
    {
        Console.WriteLine("Welcome to the Recipe Recommendation System!");
        Console.Write("Please enter your available ingredients, separated by commas: ");
        string input = Console.ReadLine();
        var userIngredients = new HashSet<string>(input.ToLower().Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries));

        var recommendedRecipes = new List<Recipe>();

        foreach (var recipe in recipes)
        {
            bool allIngredientsAvailable = true;
            foreach (var ingredient in recipe.Ingredients)
            {
                if (!userIngredients.Contains(ingredient.ToLower()))
                {
                    allIngredientsAvailable = false;
                    break;
                }
            }
            if (allIngredientsAvailable)
            {
                recommendedRecipes.Add(recipe);
            }
        }

        if (recommendedRecipes.Count > 0)
        {
            Console.WriteLine("\nBased on your ingredients, you can make the following recipes:");
            foreach (var recipe in recommendedRecipes)
            {
                Console.WriteLine($"- {recipe.Name} ({recipe.Cuisine})");
            }
        }
        else
        {
            Console.WriteLine("\nSorry, no recipes match your available ingredients at this time.");
        }
    }
}