
recipes = {
    "pasta": ["spaghetti aglio e olio", "penne arrabiata", "carbonara"],
    "soup": ["chicken noodle soup", "tomato basil soup", "miso soup"],
    "salad": ["Caesar salad", "Greek salad", "caprese salad"],
    "stir-fry": ["vegetable stir-fry", "chicken teriyaki stir-fry", "beef with broccoli stir-fry"]
}

print("Welcome to the Recipe Recommendation System!")
print("Here are some available categories:")
for category in recipes.keys():
    print(f"- {category}")

category = input("Enter a category to get recipe recommendations: ")

if category.lower() in recipes:
    print(f"Here are some recipe recommendations for {category}:")
    for recipe in recipes[category.lower()]:
        print(f"- {recipe}")
else:
    print("Sorry, that category is not available. Please choose a different category.")
