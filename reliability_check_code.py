
# dictionary of recipes with their ingredients
recipes = {
    "Spaghetti Aglio e Olio": ["spaghetti", "garlic", "olive oil", "red pepper flakes"],
    "Caprese Salad": ["tomatoes", "fresh mozzarella", "basil", "olive oil", "balsamic vinegar"],
    "Pancakes": ["flour", "milk", "eggs", "sugar", "baking powder"],
    "Caesar Salad": ["romaine lettuce", "croutons", "parmesan cheese", "Caesar dressing"],
}

# function to recommend recipes based on user's available ingredients
def recommend_recipe(available_ingredients):
    recommended_recipes = []
    for recipe, ingredients in recipes.items():
        if all(ingredient in available_ingredients for ingredient in ingredients):
            recommended_recipes.append(recipe)
    
    return recommended_recipes

# main program loop
while True:
    print("Enter the ingredients you have available (separated by commas) or type 'exit' to quit:")
    user_input = input().lower()

    if user_input == 'exit':
        break

    available_ingredients = user_input.split(",")
    recommended_recipes = recommend_recipe(available_ingredients)

    if recommended_recipes:
        print("Recommended recipes:")
        for recipe in recommended_recipes:
            print("- " + recipe)
    else:
        print("No recipes found with the available ingredients. Please try again.")
