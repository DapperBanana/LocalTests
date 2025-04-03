
# Define a dictionary of recipes with their ingredients
recipes = {
    "Spaghetti Aglio e Olio": ["spaghetti", "garlic", "olive oil", "red pepper flakes", "parsley"],
    "Chicken Alfredo": ["chicken", "fettuccine", "heavy cream", "Parmesan cheese", "butter"],
    "Caprese Salad": ["tomatoes", "mozzarella cheese", "basil", "olive oil", "balsamic vinegar"]
}

# Function to recommend a recipe based on available ingredients
def recommend_recipe(available_ingredients):
    recommended_recipe = None
    max_common_ingredients = 0
    
    for recipe, ingredients in recipes.items():
        common_ingredients = len(set(available_ingredients) & set(ingredients))
        
        if common_ingredients > max_common_ingredients:
            max_common_ingredients = common_ingredients
            recommended_recipe = recipe
    
    return recommended_recipe

# Main program
print("Welcome to the Recipe Recommendation System!")
print("Please enter the ingredients you have, separated by commas:")
available_ingredients = input().split(",")

recommended_recipe = recommend_recipe(available_ingredients)

if recommended_recipe:
    print(f"We recommend making {recommended_recipe}!")
else:
    print("Sorry, we couldn't find a recipe based on the ingredients you have.")
