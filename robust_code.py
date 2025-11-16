
# Define a list of recipes with their ingredients
recipes = {
    "Spaghetti Aglio e Olio": ["spaghetti", "garlic", "olive oil", "red pepper flakes", "parsley"],
    "Caprese Salad": ["tomatoes", "mozzarella cheese", "basil", "olive oil", "balsamic vinegar"],
    "Chicken Stir Fry": ["chicken breast", "bell peppers", "onion", "soy sauce", "ginger", "garlic"],
    "Vegetable Pasta Primavera": ["pasta", "bell peppers", "zucchini", "cherry tomatoes", "olive oil", "basil"]
}

# Function to recommend a recipe based on user's available ingredients
def recommend_recipe(available_ingredients):
    recommended_recipes = []
    for recipe, ingredients in recipes.items():
        if all(ingredient in available_ingredients for ingredient in ingredients):
            recommended_recipes.append(recipe)
    return recommended_recipes

# Get user input for available ingredients
available_ingredients = input("Enter the ingredients you have (separated by commas): ").split(",")

# Display recommended recipes
recommended_recipes = recommend_recipe([ingredient.strip() for ingredient in available_ingredients])
if recommended_recipes:
    print("Recommended recipes:")
    for recipe in recommended_recipes:
        print(recipe)
else:
    print("No recipes found with the available ingredients.")
