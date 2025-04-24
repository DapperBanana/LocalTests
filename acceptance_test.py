
# Sample recipes
recipes = {
    "Spaghetti Bolognese": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic", "olive oil"],
    "Chicken Stir-Fry": ["chicken breast", "bell peppers", "broccoli", "soy sauce", "ginger", "garlic"],
    "Caprese Salad": ["tomatoes", "fresh mozzarella", "basil", "olive oil", "balsamic vinegar", "salt"]
}

# Function to recommend recipes based on user input
def recommend_recipe(ingredients):
    recommended_recipes = []
    
    for recipe, ingredients_list in recipes.items():
        # Check if all ingredients in the recipe are in the user's input
        if all(ingredient in ingredients for ingredient in ingredients_list):
            recommended_recipes.append(recipe)
    
    return recommended_recipes

# Main program loop
while True:
    print("Enter the ingredients you have (separated by commas) or 'q' to quit:")
    user_input = input()
    
    if user_input.lower() == 'q':
        break
        
    user_ingredients = user_input.split(',')
    recommended_recipes = recommend_recipe(user_ingredients)
    
    if recommended_recipes:
        print("Recommended recipes:")
        for recipe in recommended_recipes:
            print(recipe)
    else:
        print("No recipes found with those ingredients. Try adding more ingredients.")
