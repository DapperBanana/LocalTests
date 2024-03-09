
# Dictionary of recipes with their corresponding ingredients
recipes = {
    "Pasta with Tomato Sauce": ["pasta", "tomato sauce", "garlic", "olive oil"],
    "Grilled Chicken Salad": ["chicken breast", "lettuce", "tomato", "cucumber"],
    "Vegetable Stir-Fry": ["mixed vegetables", "soy sauce", "garlic", "ginger"],
    "Avocado Toast": ["avocado", "bread", "salt", "pepper"],
    "Fruit Smoothie": ["banana", "berries", "milk", "honey"]
}

# Get input from user for their favorite ingredients
favorite_ingredients = input("Enter your favorite ingredients, separated by commas: ").split(",")

# Search for a recipe that contains all of the user's favorite ingredients
recommended_recipe = ""
for recipe, ingredients in recipes.items():
    if all(ingredient.strip().lower() in favorite_ingredients for ingredient in ingredients):
        recommended_recipe = recipe
        break

# Print the recommended recipe
if recommended_recipe != "":
    print(f"Based on your favorite ingredients, we recommend making {recommended_recipe}!")
else:
    print("Sorry, we couldn't find a recipe that matches your favorite ingredients.")
