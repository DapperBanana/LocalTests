
# Recipe recommendation system

# Sample recipes list
recipes = {
    "Pasta Carbonara": ["pasta", "bacon", "eggs", "parmesan cheese"],
    "Chicken Stir-Fry": ["chicken", "vegetables", "soy sauce", "garlic"],
    "Margherita Pizza": ["pizza dough", "tomatoes", "mozzarella cheese", "basil"]
}

# Function to recommend recipe based on ingredients
def recommend_recipe(ingredients):
    matching_recipes = []
    for recipe, recipe_ingredients in recipes.items():
        if all(ingredient in recipe_ingredients for ingredient in ingredients):
            matching_recipes.append(recipe)
    
    return matching_recipes

# Main program loop
while True:
    user_input = input("Enter ingredients (comma-separated) or type 'exit' to quit: ")
    
    if user_input.lower() == 'exit':
        break
    
    user_ingredients = user_input.split(",")
    
    recommended_recipes = recommend_recipe([ingredient.strip() for ingredient in user_ingredients])
    
    if recommended_recipes:
        print("Recommended Recipes:", recommended_recipes)
    else:
        print("No matching recipes found.")
