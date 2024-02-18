
recipes = {
    "Pasta": ["Spaghetti Aglio e Olio", "Pasta Carbonara", "Creamy Garlic Pasta"],
    "Chicken": ["Baked Chicken Parmesan", "Honey Garlic Chicken", "Garlic Butter Chicken"],
    "Salad": ["Caesar Salad", "Greek Salad", "Caprese Salad"],
    "Soup": ["Tomato Soup", "Chicken Noodle Soup", "Butternut Squash Soup"],
}

def recommend_recipe(category):
    if category in recipes:
        recommended_recipe = recipes[category][0]
        print(f"We recommend trying {recommended_recipe} for {category}.")
    else:
        print("Sorry, we don't have any recommendations for that category.")

print("Welcome to the Recipe Recommendation System!")
print("Available categories: Pasta, Chicken, Salad, Soup")

category = input("Enter a category to get a recipe recommendation: ")
recommend_recipe(category)
