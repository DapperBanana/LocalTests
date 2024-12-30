
recipes = {
    "Spaghetti Aglio e Olio": ["spaghetti", "garlic", "olive oil", "red pepper flakes", "parmesan cheese"],
    "Chicken Alfredo": ["fettuccine", "chicken breast", "heavy cream", "butter", "parmesan cheese"],
    "Caprese Salad": ["tomatoes", "mozzarella cheese", "basil leaves", "balsamic vinegar", "olive oil"]
}

def recommend_recipe(ingredients_list):
    recommended_recipes = []
    
    for recipe, ingredients in recipes.items():
        if all(item in ingredients_list for item in ingredients):
            recommended_recipes.append(recipe)
    
    if recommended_recipes:
        print("Recommended recipes based on your ingredients:")
        for recipe in recommended_recipes:
            print(recipe)
    else:
        print("No matching recipes found. Try different ingredients.")

def main():
    user_input = input("Enter a list of ingredients separated by commas: ").split(",")
    ingredients_list = [ingredient.strip().lower() for ingredient in user_input]

    recommend_recipe(ingredients_list)

if __name__ == "__main__":
    main()
