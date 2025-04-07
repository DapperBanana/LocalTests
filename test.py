
# Define a list of recipes with their ingredients
recipes = {
    "Pasta with Tomato Sauce": ["pasta", "tomato sauce", "garlic", "onion"],
    "Grilled Chicken Salad": ["chicken breast", "lettuce", "tomato", "cucumber"],
    "Vegetable Stir Fry": ["mixed vegetables", "soy sauce", "ginger", "garlic"],
    "Banana Bread": ["bananas", "flour", "sugar", "eggs", "baking powder"]
}

# Function to recommend recipes based on user input
def recommend_recipe(ingredients):
    recommended_recipes = []
    for recipe, ingredients_list in recipes.items():
        if all(ingredient in ingredients for ingredient in ingredients_list):
            recommended_recipes.append(recipe)
    return recommended_recipes

# Main program
print("Welcome to the Recipe Recommendation System!")
print("Please enter the ingredients you have, separated by commas:")
user_input = input().split(",")

recommended_recipes = recommend_recipe(user_input)

if recommended_recipes:
    print("Based on the ingredients you have, we recommend the following recipes:")
    for recipe in recommended_recipes:
        print(recipe)
else:
    print("Sorry, we could not find any recipes based on the ingredients you have.")
