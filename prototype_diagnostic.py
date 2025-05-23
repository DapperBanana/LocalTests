
# Recipe Recommendation System

recipes = {
    "Spaghetti Bolognese": ["spaghetti", "minced beef", "tomato sauce", "onion", "garlic", "herbs", "parmesan cheese"],
    "Chicken Stir Fry": ["chicken breast", "vegetables", "soy sauce", "garlic", "ginger", "rice"],
    "Caesar Salad": ["romaine lettuce", "croutons", "parmesan cheese", "caesar dressing", "chicken breast"]
}

def recommend_recipe(ingredients):
    recommended_recipes = []
    
    for recipe, recipe_ingredients in recipes.items():
        if all(ingredient in ingredients for ingredient in recipe_ingredients):
            recommended_recipes.append(recipe)
    
    return recommended_recipes

print("Welcome to the Recipe Recommendation System!")
print("Enter the ingredients you have, separated by commas:")
user_input = input()
user_ingredients = user_input.lower().split(",")

recommended_recipes = recommend_recipe(user_ingredients)

if recommended_recipes:
    print("Here are some recipes you can make with the ingredients you have:")
    for recipe in recommended_recipes:
        print(recipe)
else:
    print("Sorry, we couldn't find any recipes with the ingredients you have.")
