
recipes = {
    "pasta": ["Spaghetti Aglio e Olio", "Pasta Carbonara", "Creamy Pesto Pasta"],
    "salad": ["Greek Salad", "Caesar Salad", "Caprese Salad"],
    "soup": ["Tomato Soup", "Chicken Noodle Soup", "Vegetable Soup"]
}

print("Welcome to the Recipe Recommendation System!")
print("Please choose a category: pasta, salad, or soup")

category = input("Enter a category: ")

if category.lower() in recipes:
    print("Here are some recipe recommendations for", category.capitalize(), ":")
    for recipe in recipes[category.lower()]:
        print(recipe)
else:
    print("Sorry, we don't have any recommendations for that category.")
