
import random

# dictionary of recipes with their ingredients
recipes = {
    "Pasta Carbonara": ["pasta", "eggs", "bacon", "parmesan cheese"],
    "Chicken Stir Fry": ["chicken", "vegetables", "soy sauce", "garlic"],
    "Spaghetti Bolognese": ["spaghetti", "ground beef", "tomato sauce", "onion"],
    "Caesar Salad": ["romaine lettuce", "croutons", "parmesan cheese", "Caesar dressing"]
}

# function to recommend a random recipe based on ingredients provided
def recommend_recipe(ingredients):
    possible_recipes = []
    for recipe, recipe_ingredients in recipes.items():
        if all(ingredient in recipe_ingredients for ingredient in ingredients):
            possible_recipes.append(recipe)
    
    if possible_recipes:
        return random.choice(possible_recipes)
    else:
        return "No recipe found with given ingredients."

# main program
print("Welcome to the Recipe Recommendation System!")

while True:
    print("\nHere are the available recipes:")
    for i, recipe in enumerate(recipes.keys(), 1):
        print(f"{i}. {recipe}")
    
    choice = input("\nEnter ingredients you have (separated by commas): ").lower().split(",")
    recommended_recipe = recommend_recipe(choice)
    
    print(f"\nBased on the ingredients you have, we recommend trying: {recommended_recipe}")
    
    again = input("\nDo you want to find another recipe? (yes/no): ")
    if again.lower() != "yes":
        break

print("\nThank you for using the Recipe Recommendation System!")
