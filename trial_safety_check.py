
recipes = {
    "spaghetti": ["spaghetti noodles", "tomato sauce", "ground beef", "garlic", "onion", "salt", "pepper"],
    "pancakes": ["flour", "eggs", "milk", "baking powder", "sugar", "salt", "butter"],
    "grilled cheese sandwich": ["bread", "cheese", "butter"]
}

def recommend_recipe(ingredients):
    recommended_recipes = []
    for recipe, recipe_ingredients in recipes.items():
        if all(ingredient in recipe_ingredients for ingredient in ingredients):
            recommended_recipes.append(recipe)
    
    if recommended_recipes:
        print("Recommended recipes:")
        for recipe in recommended_recipes:
            print(recipe)
    else:
        print("No recipes found with the provided ingredients.")

def main():
    print("Welcome to the Recipe Recommendation System!")
    
    while True:
        user_input = input("Enter a list of ingredients (separated by comma): ")
        if user_input == "exit":
            break
        
        ingredients = [ingredient.strip() for ingredient in user_input.split(",")]
        
        recommend_recipe(ingredients)

if __name__ == "__main__":
    main()
